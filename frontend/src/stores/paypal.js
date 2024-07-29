import { defineStore } from "pinia";
import { create_request } from "./services/request_http";

export const usePayPalStore = defineStore("payPalStore", {
    state: () => ({
        orderID: null,
        isPaymentApproved: false,
        isOrderCompleted: false,
        isLoading: false,
        error: null,
    }),
    actions: {
        /**
         * Creates a PayPal order with the specified amount.
         * 
         * @param {number} amount - The amount for the PayPal order.
         * @returns {Promise<string>} - A promise that resolves to the order ID.
         * @throws {Error} - Throws an error if the order creation fails.
         */
        async createOrder(amount) {
            this.isLoading = true;
            this.error = null;
            try {
                const response = await create_request("create-order/", { amount });
                this.orderID = response.data.orderID;
                this.isLoading = false;
                return this.orderID;
            } catch (error) {
                this.error = error.response.data;
                this.isLoading = false;
                throw error;
            }
        },

        /**
         * Submits the form and captures the PayPal order.
         * 
         * @param {Object} form - The form data.
         * @param {string} form.email - The email address.
         * @param {string} form.address - The address.
         * @param {string} form.city - The city.
         * @param {string} form.state - The state.
         * @param {string} form.postalCode - The postal code.
         * @param {Array} form.soldProducts - The sold products.
         * @returns {Promise<number>} - A promise that resolves to the response status.
         * @throws {Error} - Throws an error if the capture fails.
         */
        async submitFormAndCaptureOrder(form) {
            this.isLoading = true;
            this.error = null;
            try {
                const response = await create_request("capture-order/", { 
                    orderID: this.orderID, 
                    email: form.email,
                    address: form.address,
                    city: form.city,
                    state: form.state,
                    postal_code: form.postalCode,
                    sold_products: form.soldProducts,
                });
                this.isLoading = false;
                return response.status;
            } catch (error) {
                this.error = error;
                this.isLoading = false;
                throw error;
            }
        }
    }
});
