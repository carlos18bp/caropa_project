<template>
    <!-- Carousel container for trending products -->
    <div v-if="productsOnTrending" class="carousel-container px-8 max-w-7xl mx-auto py-16">
        <div class="text-center mb-8">
            <h2 class="text-3xl font-semibold test-thirdSection-title">
                {{ $t('thirdSection').title }}
            </h2>
            <p class="text-xl font-medium text-gray-500">
                <span class="test-thirdSection-subtitle">
                    {{ $t('thirdSection').subtitle }}
                </span> |
                <span class="border-b-2 border-b-gray-500 test-shopNow">
                    {{ $t('shopNow') }}
                </span>
            </p>
        </div>
        <div class="relative">
            <Swiper 
            ref="swiper"
            :modules="modules" 
            :loop="true"
            :breakpoints="{
                640: {
                    slidesPerView: 1,
                    spaceBetween: 20,
                },
                768: {
                    slidesPerView: 2,
                    spaceBetween: 40,
                },
                1024: {
                    slidesPerView: 4,
                    spaceBetween: 50,
                },
            }" 
            :autoplay="{
                delay: 4000,
                disableOnInteraction: false,
            }" 
            class="w-full h-full"
            >
                <swiper-slide v-for="product in productsOnTrending">
                    <img :src="product.gallery_urls[0]">
                    <h2 v-if="currentLanguage === 'en'" class="text-center text-xl font-medium mt-4">{{ product.product_detail.name_en }}</h2>
                    <h2 v-else class="text-center text-xl font-medium mt-4">{{ product.product_detail.name_es }}</h2>
                    <h3 class="text-center text-xl font-medium mt-4">$ {{ product.product_detail.price }}</h3>
                </swiper-slide>
            </Swiper>
        </div>
    </div>
</template>

<script setup>
    // Importing necessary modules
    import { computed, ref, onMounted, watchEffect } from "vue";
    import { useAppStore } from '@/stores/language.js';
    import { useProductStore } from "@/stores/product";
    import { Autoplay } from "swiper/modules";
    import { Swiper, SwiperSlide } from "swiper/vue";
    import enMessages from "@/locales/home/en";
    import esMessages from "@/locales/home/es";

    import "swiper/css";

    // Functions necessary for Swiper
    const modules = [Autoplay];

    // Initializing state
    const productsOnTrending = ref(null);

    // Access the current language from the store
    const appStore = useAppStore();
    const currentLanguage = computed(() => appStore.getCurrentLanguage);
    const messages = ref(enMessages)

    // Access the product store to get trending products
    const productStore = useProductStore();

    // Translation function
    const $t = (key) => messages.value[key];

    // Change messages in function to currently language
    watchEffect(() => {
        messages.value = currentLanguage.value === "en" ? enMessages : esMessages;
    });

    // Fetch products when the component is mounted
    onMounted(async () => {
        await productStore.fetchProducts();
        productsOnTrending.value = productStore.trendingProducts;
    });

</script>
