<template>
    <div>
        <!-- Header component -->
        <Header></Header>

        <!-- Carousel section -->
        <section class="w-full h-screen">
            <swiper v-if="home" :modules="modules" :loop="true" :pagination="pagination" :autoplay="{
                delay: 4000,
                disableOnInteraction: false,
            }" class="w-full h-full">
                <swiper-slide class="flex justify-center items-center"
                    v-for="image in home.carousel_presentation_urls" :key="image">
                    <img class="block w-full h-full object-cover" :src="image" />
                </swiper-slide>
            </swiper>
        </section>

        <!-- First category section -->
        <section class="max-w-7xl mx-auto py-16">
            <div class="grid md:grid-cols-2 gap-4">
                <div v-for="category in home_categories.slice(0, 2)" :key="category.id">
                    <div>
                        <h1 class="text-black font-semibold text-3xl text-center">
                            <span v-if="currentLanguage === 'en'">
                                {{ category.title_en }}
                            </span>
                            <span v-else>{{ category.title_es }}</span>
                        </h1>
                        <h2 class="text-black font-light text-lg text-center test-shopNow">{{ $t('shopNow') }}</h2>
                    </div>
                    <div class="flex justify-center pt-6">
                        <img class="w-3/4 rounded-full lg:rounded-none lg:w-full" :src="category.image"
                            :alt="'Image from Caropa Couture about ' + category.title_en" />
                    </div>
                </div>
            </div>
        </section>

        <!-- Different occasions section -->
        <section class="px-8 max-w-7xl mx-auto py-16 lg:px-0">
            <div>
                <h1 class="text-black font-semibold text-3xl text-center test-firstSection-title">
                    {{ $t('firstSection').title }}
                </h1>
                <h2 class="text-black font-medium text-xl text-center test-firstSection-subtitle">
                    {{ $t('firstSection').subtitle }} | <span class="border-b-2 border-b-black uppercase test-shopNow">{{ $t('shopNow') }}</span>
                </h2>
            </div>
            <div class="mt-16 grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
                <div v-for="category in home_categories.slice(2, 8)" :key="category.id">
                    <h2 class="text-black font-semibold text-lg text-center">
                        <span v-if="currentLanguage === 'en'">
                            {{ category.title_en }}
                        </span>
                        <span v-else>{{ category.title_es }}</span>
                    </h2>
                    <img class="w-full mt-4" :src="category.image"
                        :alt="'Image from Caropa Couture about ' + category.title_en" />
                    <h3 class="text-gray-500 text-md text-center font-semibold mt-4 test-shopNow">
                        {{ $t('shopNow') }}
                    </h3>
                </div>
            </div>
        </section>

        <!-- Gallery and description section -->
        <section v-if="home" class="max-w-7xl px-8 mx-auto py-16 grid gap-6 lg:grid-cols-2">
            <swiper :modules="modules" :loop="true" :pagination="pagination" :autoplay="{
                delay: 3000,
                disableOnInteraction: false,
            }" class="w-full h-full">
                <swiper-slide class="flex justify-center items-center" v-for="image in home.section_3_gallery_urls" :key="image">
                    <img class="block w-full h-full object-cover" :src="image" />
                </swiper-slide>
            </swiper>
            <div class="flex justify-center items-center">
                <div>
                    <h1 class="font-semibold text-black text-4xl text-center">
                        <span v-if="currentLanguage === 'en'">
                            {{ home.section_3_title_en }}
                        </span>
                        <span v-else>{{ home.section_3_title_es }}</span>
                    </h1>
                    <h2 class="font-semibold text-gray-400 text-xl text-center mt-4">
                        <span v-if="currentLanguage === 'en'">
                            {{ home.section_3_description_en }}
                        </span>
                        <span v-else>{{ home.section_3_description_es }}</span>
                    </h2>
                    <h3 class="font-semibold text-gray-400 text-xl text-center mt-4 test-secondSection-subtitle">
                        {{ $t('secondSection').subtitle }}
                        <span class="border-b-2 border-b-gray-400 test-secondSection-subtitle">{{ $t('secondSection').click }}</span>
                    </h3>
                </div>
            </div>
        </section>

        <!-- Second category section -->
        <section class="max-w-7xl px-8 mx-auto py-16">
            <div class="grid md:grid-cols-2 gap-4">
                <div v-for="category in home_categories.slice(8, 12)" :key="category.id">
                    <div>
                        <h1 class="text-black font-semibold text-lg text-center">
                            <span v-if="currentLanguage === 'en'">
                                {{ category.title_en }}
                            </span>
                            <span v-else>{{ category.title_es }}</span>
                        </h1>
                        <h2 class="text-black font-light text-md text-center test-shopNow">{{ $t('shopNow') }}</h2>
                    </div>
                    <div class="flex justify-center pt-6">
                        <img class="w-full" :src="category.image"
                            :alt="'Image from Caropa Couture about ' + category.title_en" />
                    </div>
                </div>
            </div>
        </section>

        <!-- Product carousel component -->
        <ProductCarousel></ProductCarousel>
        <!-- About shortcut component -->
        <AboutShortCut></AboutShortCut>
        <!-- Footer component -->
        <Footer></Footer>
    </div>
</template>

<script setup>
    // Importing necessary modules and components
    import { computed, ref, onMounted, watchEffect } from "vue";
    import { Pagination, Autoplay } from "swiper/modules";
    import { Swiper, SwiperSlide } from "swiper/vue";
    import { useAppStore } from '@/stores/language.js';
    import { useHomeStore } from "@/stores/home";
    
    import AboutShortCut from "@/components/AboutShortCut.vue";
    import Footer from "@/components/layouts/Footer.vue";
    import Header from "@/components/layouts/Header.vue";
    import ProductCarousel from "@/components/ProductCarousel.vue";

    import enMessages from "@/locales/home/en";
    import esMessages from "@/locales/home/es";

    import "swiper/css";
    import "swiper/css/pagination";

    // Initialize store instances and state variables
    const appStore = useAppStore();
    const homeStore = useHomeStore();
    const currentLanguage = computed(() => appStore.getCurrentLanguage);
    const home = ref(null);
    const home_categories = ref([]);
    const modules = [Pagination, Autoplay];
    const pagination = {
        clickable: true,
    };
    const messages = ref(enMessages)

    // Translation function
    const $t = (key) => messages.value[key];

    // Change messages in function to currently language
    watchEffect(() => {
        messages.value = currentLanguage.value === "en" ? enMessages : esMessages;
    });

    // Fetch home data when the component is mounted
    onMounted(async () => {
        await homeStore.fetchHome();
        home.value = homeStore.home;
        home_categories.value = homeStore.home_categories;
    });
</script>

<style>
    /* Custom styles for the Swiper pagination bullets */
    .swiper-pagination-bullet {
        background-color: transparent;
        border: 1px solid #fff;
        opacity: 100;
        width: 12px;
        height: 12px;
    }

    .swiper-pagination-bullet-active {
        background-color: #fff;
        width: 12px;
        height: 12px;
    }
</style>
