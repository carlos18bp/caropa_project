<template>
    <Header></Header>
    <div class="max-w-7xl px-8 mx-auto my-16 space-y-12">
        <div class="grid lg:grid-cols-2">

            <!-- Text content -->
            <div>
                <h2 class="text-2xl font-medium mb-4 test-firstSection-whoWeAre-title">{{ $t('firstSection').whoWeAre.title }}</h2>
                <p class="mb-4 font-regular test-firstSection-whoWeAre-paragraph">
                    {{ $t('firstSection').whoWeAre.paragraph }}
                </p>
                <h2 class="text-2xl font-medium mb-4 test-firstSection-ourStory-title">{{ $t('firstSection').ourStory.title }}</h2>
                <p class="mb-4 font-regular test-firstSection-ourStory-paragraphOne" v-html=" $t('firstSection').ourStory.paragraphOne ">
                </p>
                <p class="mb-4 font-regular test-firstSection-ourStory-paragraphTwo">
                    {{ $t('firstSection').ourStory.paragraphTwo }}
                </p>
                <p class="mb-4 font-regular test-firstSection-ourStory-paragraphThree">
                    {{ $t('firstSection').ourStory.paragraphThree }}
                </p>
                <p class="mb-4 font-regular test-firstSection-ourStory-paragraphFour">
                    {{ $t('firstSection').ourStory.paragraphFour }}
                </p>
            </div>

            <!-- Image content -->
            <div class="relative">
                <img src="@/assets/images/about_us/image1.png" alt="About us" class="sticky top-0 rounded-full object-cover w-2/3 mx-auto" />
            </div>
        </div>
        <div class="grid lg:grid-cols-2">

            <!-- Image content -->
            <div class="relative order-2 lg:order-1">
                <img src="@/assets/images/about_us/image2.png" alt="Blue Mom partnership"
                    class="sticky top-0 mx-auto rounded-full shadow-lg object-cover w-2/3" />
            </div>

            <!-- Text content -->
            <div class="text-right order-1 lg:order-2">
                <div class="mb-4 flex items-center gap-2 justify-end">
                    <h2 class="text-2xl font-medium">BLUE MOM</h2>
                    <div>
                        <img src="@/assets/images/icons/heart.png" alt="Icon blue heart" class="w-4">
                    </div>
                </div>
                <p class="mb-4 font-regular">
                    {{ $t('secondSection').blueMom.paragraphOne }}
                </p>
                <p class="mb-4 font-regular">
                    {{ $t('secondSection').blueMom.paragraphTwo }}
                </p>
                <p class="mb-4 font-regular">
                    {{ $t('secondSection').blueMom.paragraphThree }}
                </p>
            </div>
        </div>
    </div>
    <Footer></Footer>
</template>

<script setup>
    import { ref, watchEffect, computed } from "vue";

    import Header from "@/components/layouts/Header.vue";
    import Footer from "@/components/layouts/Footer.vue";

    import { useAppStore } from '@/stores/language.js';
    import enMessages from "@/locales/about/en";
    import esMessages from "@/locales/about/es";

    // Initialize store and get current language
    const appStore = useAppStore();
    const currentLanguage = computed(() => appStore.getCurrentLanguage);
    const messages = ref(enMessages)

    // Translation function
    const $t = (key) => messages.value[key];

    // Change messages in function to currently language
    watchEffect(() => {
        messages.value = currentLanguage.value === "en" ? enMessages : esMessages;
    });

</script>
