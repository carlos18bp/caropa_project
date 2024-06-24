<template>
    <!-- Footer section with black background -->
    <footer class="bg-black" aria-labelledby="footer-heading">

        <!-- Invisible heading for accessibility -->
        <h2 id="footer-heading" class="sr-only">Footer</h2>
        <div class="mx-auto max-w-7xl px-6 pb-8 pt-16 sm:pt-24 lg:px-8 lg:pt-32">
            <div class="xl:grid xl:grid-cols-3 xl:gap-8">

                <!-- Logo and company description -->
                <div class="space-y-8">
                    <img src="@/assets/images/logo2.png" alt="Logo of Caropa Couture">
                    <p class="text-md font-medium leading-6 text-white">
                        Redefining fashion with exclusive,<br>fresh style and a unique personality.
                    </p>

                    <!-- Social media icons -->
                    <div class="flex space-x-6">
                        <a href="#" class="text-white hover:text-gray-400">
                            <span class="sr-only">Facebook</span>
                            <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                                <path fill-rule="evenodd" d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z" clip-rule="evenodd" />
                            </svg>
                        </a>
                        <a href="#" class="text-white hover:text-gray-400">
                            <span class="sr-only">Instagram</span>
                            <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                                <path fill-rule="evenodd" d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63zm-.081 1.802h-.468c-2.456 0-2.784.011-3.807.058-.975.045-1.504.207-1.857.344-.467.182-.8.398-1.15.748-.35.35-.566.683-.748 1.15-.137.353-.3.882-.344 1.857-.047 1.023-.058 1.351-.058 3.807v.468c0 2.456.011 2.784.058 3.807.045.975.207 1.504.344 1.857.182.466.399.8.748 1.15.35.35.683.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058h.08c2.597 0 2.917-.01 3.96-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.683.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041v-.08c0-2.597-.01-2.917-.058-3.96-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.023-.047-1.351-.058-3.807-.058zM12 6.865a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 1.802a3.333 3.333 0 100 6.666 3.333 3.333 0 000-6.666zm5.338-3.205a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z" clip-rule="evenodd" />
                            </svg>
                        </a>
                    </div>
                </div>
                <!-- Navigation and company links -->
                <div class="mt-16 grid grid-cols-2 gap-8 xl:col-span-2 xl:mt-0">
                    <div class="md:grid md:grid-cols-2 md:gap-8">
                        <div>
                            <h3 class="text-sm font-medium leading-6 text-white">COMPANY</h3>
                            <ul role="list" class="mt-6 grid grid-cols-1 gap-4 font-regular text-white text-sm">
                                <li>
                                    <a @click="goTo('catalog')" class="cursor-pointer">Shop</a>
                                </li>
                                <li>
                                    <a @click="goTo('about_us')" class="cursor-pointer">About Us</a>
                                </li>
                                <li>
                                    <a @click="showContactModel = true" class="cursor-pointer">
                                        Contact
                                    </a>
                                </li>
                                <li>
                                    <a href="#" class="cursor-pointer">Blue Mom</a>
                                </li>
                            </ul>
                        </div>
                        <div class="mt-10 md:mt-0">
                            <h3 class="text-sm font-medium leading-6 text-white">NAVIGATE</h3>
                            <ul role="list" class="mt-6 grid grid-cols-2 gap-4 font-regular text-white text-sm">
                                <li v-for="category in categories" :key="category">
                                    <a @click="filterProducts(category)" class="cursor-pointer">
                                        {{ category }}
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div class="md:grid md:grid-cols-2 md:gap-8">
                        <div>
                            <h3 class="text-sm font-semibold leading-6 text-white">LEGAL</h3>
                            <ul role="list" class="mt-6 space-y-4 font-regular text-white text-sm">
                                <li>
                                    <a href="#" class="leading-6">Terms & Conditions</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Footer bottom section -->
            <div class="mt-16 border-t border-white/10 pt-8 sm:mt-20 lg:mt-24">
                <p class="text-sm font-medium leading-5 text-white">&copy; 2020 Caropa Couture. All rights reserved</p>
            </div>
        </div>
    </footer>

    <!-- Contact modal component -->
    <div v-if="showContactModel" class="fixed z-30 w-full h-screen top-0">
        <ContactModel :visible="showContactModel" @update:visible="showContactModel = $event"></ContactModel>
    </div>
</template>

<script setup>
    // Importing necessary modules and components
    import { computed, onMounted, ref } from 'vue';
    import ContactModel from "@/components/ContactModel.vue";
    import { useAppStore } from '@/stores/language.js';
    import { useProductStore } from "@/stores/product";
    import { useRouter, useRoute } from 'vue-router';

    const showContactModel = ref(false)
    // Initialize app store to access the current language
    const appStore = useAppStore();
    const currentLanguage = computed(() => appStore.getCurrentLanguage);

    // Initialize product store to access products and categories
    const productStore = useProductStore();
    const categories = computed(() => productStore.primaryCategories(currentLanguage.value));

    // Router instance
    const router = useRouter();
    const route = useRoute();

    // Fetch products when component is mounted
    onMounted(async () => {
        await productStore.fetchProducts();
    });

    /**
     * Navigate to a different route
     * @param {String} route - The name of the route to navigate to
     */
    const goTo = (route) => {
        router.push({ name: route });
        scrollToTop();
    };

    /**
     * Filters products based on the selected category
     * @param {String} category - The selected category
     */
    const filterProducts = (category) => {
        if (route.name !== 'catalog') {
            router.push({ name: 'catalog' });
        }
        scrollToTop();
        productStore.primaryCategorySeleted = category;
        productStore.filterProductsByCategory(currentLanguage.value);
    };

    /**
     * Scroll to the top of the page smoothly
     */
    const scrollToTop = () => {
        const scrollDuration = 2500; // Duration in milliseconds
        const scrollStep = -window.scrollY / (scrollDuration / 15);
        const scrollInterval = setInterval(() => {
            if (window.scrollY !== 0) {
                window.scrollBy(0, scrollStep);
            } else {
                clearInterval(scrollInterval);
            }
        }, 15);
    };
</script>
