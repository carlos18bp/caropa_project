<template>
  <div>
    <Banner></Banner>
    <Header></Header>
    <section class="w-full h-screen">
      <swiper :modules="modules" :loop="true" :pagination="pagination" :autoplay="{
        delay: 4000,
        disableOnInteraction: false,
      }" class="w-full h-full">
        <swiper-slide class="flex justify-center items-center" v-if="home"
          v-for="image in home.carousel_presentation_urls">
          <img class="block w-full h-full object-cover" :src="image" />
        </swiper-slide>
      </swiper>
    </section>
    <section class="px-72 py-16">
      <div class="grid grid-cols-2 gap-4">
        <div v-for="(category, index) in home_categories.slice(0, 2)" :key="category.id">
          <div>
            <h1 class="text-black font-semibold text-3xl text-center">
              {{ category.title }}
            </h1>
            <h2 class="text-black font-light text-lg text-center">Shop Now</h2>
          </div>
          <div class="flex justify-center pt-6">
            <img class="w-full" :src="category.image" :alt="'Image from Caropa Couture about ' + category.title" />
          </div>
        </div>
      </div>
    </section>
    <section class="px-72 py-16">
      <div>
        <h1 class="text-black font-semibold text-3xl text-center">
          DIFFERENT OCCASIONS
        </h1>
        <h2 class="text-black font-medium text-xl text-center">
          Your one-stop destination for every style, trend, and occasion.
          Explore now | <span class="border-b-2 border-b-black">SHOP NOW</span>
        </h2>
      </div>
      <div class="mt-16 grid grid-cols-3 gap-4">
        <div v-for="(category, index) in home_categories.slice(2, 8)" :key="category.id">
          <h2 class="text-black font-semibold text-lg text-center">
            {{ category.title }}
          </h2>
          <img class="w-full mt-4" :src="category.image" :alt="'Image from Caropa Couture about ' + category.title" />
          <h3 class="text-gray-500 text-md text-center font-semibold mt-4">
            SHOP NOW
          </h3>
        </div>
      </div>
    </section>
    <section v-if="home" class="px-72 py-16 grid grid-cols-2">
      <swiper :modules="modules" :loop="true" :pagination="pagination" :autoplay="{
        delay: 3000,
        disableOnInteraction: false,
      }" class="w-full h-full">
        <swiper-slide class="flex justify-center items-center" v-for="image in home.section_3_gallery_urls">
          <img class="block w-full h-full object-cover" :src="image" />
        </swiper-slide>
      </swiper>
      <div class="flex justify-center items-center">
        <div>
          <h1 class="font-semibold tect-black text-4xl text-center">
            {{ home.section_3_title }}
          </h1>
          <h2 class="font-semibold text-gray-400 text-xl text-center mt-4">
            {{ home.section_3_description }}
          </h2>
          <h3 class="font-semibold text-gray-400 text-xl text-center mt-4">
            Want to explore more?
            <span class="border-b-2 border-b-gray-400">Click here now!</span>
          </h3>
        </div>
      </div>
    </section>
    <section class="px-72 py-16">
      <div class="grid grid-cols-2 gap-4">
        <div v-for="(category, index) in home_categories.slice(8, 12)" :key="category.id">
          <div>
            <h1 class="text-black font-semibold text-lg text-center">
              {{ category.title }}
            </h1>
            <h2 class="text-black font-light text-md text-center">Shop Now</h2>
          </div>
          <div class="flex justify-center pt-6">
            <img class="w-full" :src="category.image" :alt="'Image from Caropa Couture about ' + category.title" />
          </div>
        </div>
      </div>
    </section>
    <ProductCarousel></ProductCarousel>
    <AboutShortCut></AboutShortCut>
    <Footer></Footer>
  </div>
</template>

<script setup>
  import Banner from "@/components/layouts/Banner.vue";
  import Header from "@/components/layouts/Header.vue";
  import Footer from "@/components/layouts/Footer.vue";
  import ProductCarousel from "@/components/ProductCarousel.vue";
  import AboutShortCut from "@/components/AboutShortCut.vue";
  import { useHomeStore } from "@/stores/home";
  import { ref, onMounted } from "vue";
  import { Swiper, SwiperSlide } from "swiper/vue";
  import "swiper/css";
  import "swiper/css/pagination";
  import { Pagination, Autoplay } from "swiper/modules";

  const homeStore = useHomeStore();
  const home = ref(null);
  const home_categories = ref([]);
  const modules = [Pagination, Autoplay];
  const pagination = {
    clickable: true,
  };

  onMounted(async () => {
    await homeStore.fetchHome();
    home.value = homeStore.home;
    home_categories.value = homeStore.home_categories;
  });
</script>

<style>
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
