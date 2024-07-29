<template>
    <div id="paypal-button-container"></div>
</template>

<script setup>
    import { onMounted } from 'vue';
    import { usePayPalStore } from '@/stores/paypal.js';
    import Swal from 'sweetalert2';

    // Use PayPal store
    const paypalStore = usePayPalStore();

    // Define emitted events
    const emit = defineEmits(['payment-approved', 'validate-form']);

    /**
     * Define the properties that the component will receive.
     * In this case, the amount for the payment.
     */
    const props = defineProps({
        amount: {
            type: Number,
            required: true
        },
    });

    /**
     * Executes when the component is mounted.
     * Here we initialize the PayPal button.
     */
    onMounted(() => {
        paypal.Buttons({
            /**
             * Create order function that sends a request to the backend
             * to create a PayPal order with the specified amount.
             * 
             * @returns {Promise<string>} - A promise that resolves to the order ID.
             */
            createOrder: async () => {
                // Validate the form before creating the order
                const isFormValid = await new Promise((resolve) => {
                    emit('validate-form', (isValid) => {
                        resolve(isValid);
                    });
                });

                // Proceed if the form is valid
                if (isFormValid) {
                    try {
                        const orderID = await paypalStore.createOrder(props.amount);
                        return orderID;
                    } catch (error) {
                        console.error('Error creating order:', error);
                        return '';
                    }
                } else {
                    // Show an alert if the form is not complete
                    Swal.fire({
                        icon: 'error',
                        title: 'Form Missing',
                        text: "It's necessary to complete the whole form.",
                        iconColor: '#FFF',
                        customClass: {
                            popup: 'bg-primary',
                            icon: 'bg-primary',
                            title: 'font-regular text-white',
                            confirmButton: 'bg-white text-primary font-regular py-2 px-4 rounded-lg outline-none',
                        },
                        buttonsStyling: false,
                        didOpen: () => {
                            paypalStore.orderID = null;
                            paypalStore.isPaymentApproved = false;
                            paypalStore.isOrderCompleted = false;
                            paypalStore.isLoading = false;
                            paypalStore.error = null;
                        }
                    });
                }
            },
            /**
             * On approve function that captures the order once the user approves the payment.
             * 
             * @param {Object} data - Data object containing the order ID.
             * @param {Object} actions - Actions object.
             */
            onApprove: async (data) => {
                try {
                    // Mark the payment as approved and emit the event
                    paypalStore.isPaymentApproved = true;
                    emit('payment-approved');
                } catch (error) {
                    console.error('Error capturing order:', error);
                }
            }
        }).render('#paypal-button-container');
    });
</script>
