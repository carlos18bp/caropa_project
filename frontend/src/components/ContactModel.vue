<template>
    <div v-if="visible" class="fixed inset-0 flex items-center z-50">
        <div 
            ref="background"
            @click="closeContact()" 
            class="absolute inset-0 bg-gray-500 bg-opacity-40 backdrop-blur-md">
        </div>
        <div ref="modal" class="relative w-full h-fit max-w-md md:max-w-lg lg:max-w-2xl mx-auto bg-white rounded-lg">
                <!-- Modal header -->
                <div class="flex items-start justify-between p-5 pb-0">
                    <h3 class="text-2xl font-semibold text-black lg:text-4xl test-contact-getInTouch">
                        {{ $t('contact').getInTouch }}
                    </h3>
                    <XMarkIcon @click="closeContact()" class="text-gray-500 cursor-pointer w-6 h-6">
                    </XMarkIcon>
                </div>

                <!-- Modal body -->
                <div class="p-6">
                    <div class="flex items-center pb-4">
                        <div class="flex items-center w-8">
                            <img src="@/assets/images/icons/phone_call.png" class="size-8" />
                        </div>
                        <a href="tel:+17543999909" class="text-xl pl-2 font-regular">+1 (754) 399-9909</a>
                    </div>
                    <div class="flex items-center pb-4">
                        <div class="flex items-center w-8">
                            <img src="@/assets/images/icons/sharp_email.png" class="size-8" />
                        </div>
                        <a href="mailto:info@caropacouture.com" class="text-xl pl-2 font-regular">info@caropacouture.com</a>
                    </div>
                    <div class="flex items-center">
                        <div class="flex items-center w-8">
                            <img src="@/assets/images/icons/location.png" class="size-8" />
                        </div>
                        <p class="text-xl ml-2 font-regular">
                            9620 Stirling RD Unit 4-103 Cooper City, Fl 33024
                        </p>
                    </div>
                </div>

                
                <div class="w-full h-40">
                    <GoogleMap
                        api-key="AIzaSyD7cf5pD4u32w9k2zEnjq19nd8WlGmm-ls"
                        class="h-full"
                        :center="center"
                        :zoom="9"
                    >
                        <Marker :options="{ position: center }" />
                    </GoogleMap>
                </div>

                <div class="flex justify-evenly p-6 pb-8">
                    <a href="#">
                        <i class="bi bi-facebook text-4xl"></i>
                    </a>
                    <a href="#">
                        <i class="bi bi-instagram text-4xl"></i>
                    </a>
                </div>
        </div>
    </div>
</template>

<script setup>
    import { ref, watchEffect, computed } from 'vue';
    import { GoogleMap, Marker } from "vue3-google-map";
    import { XMarkIcon } from "@heroicons/vue/24/outline";
    import gsap from "gsap";

    import { useAppStore } from '@/stores/language.js';
    import enMessages from "@/locales/layouts/header/en";
    import esMessages from "@/locales/layouts/header/es";

    // Initialize app store to access the current language
    const appStore = useAppStore();
    const currentLanguage = computed(() => appStore.getCurrentLanguage);
    const messages = ref(enMessages)

    const background = ref(null);
    const modal = ref(null)

    const center = {
        lat: 25.850760259291917, 
        lng: -80.2099832472325
    }

    const props = defineProps({
        visible: {
            type: Boolean,
            required: true
        }
    });

    const $t = (key) => messages.value[key];
    
    const emit = defineEmits(['update:visible']);

    watchEffect(() => {
        messages.value = currentLanguage.value === "en" ? enMessages : esMessages;
        if (props.visible) {
            document.body.style.overflow = "hidden";
            if (background.value) {
                gsap.fromTo(
                    background.value,
                    {
                        opacity: 0,
                    },
                    {
                        opacity: 1,
                        duration: 1,
                        ease: "power2.inOut",
                    }
                );
            }
            if (modal.value) {
                gsap.fromTo(
                    modal.value,
                    {
                        opacity: 0,
                    },
                    {
                        opacity: 1,
                        duration: 1,
                        ease: "power2.inOut",
                    }
                );
            }
        }
    })

    const closeContact = () => {
        const modalAnimation = gsap
            .to(
                modal.value,
                {
                    opacity: 0,
                    duration: 1,
                    ease: "power2.inOut",
                }
            )
        const backgroundAnimation = gsap
            .to(
                background.value,
                {
                    opacity: 0,
                    duration: 1,
                    ease: "power2.inOut",
                }
            )
            .then();

        // Wait while both are finished
        Promise.all([ modalAnimation, backgroundAnimation ]).then(() => {
            document.body.style.overflow = "auto";
            emit("update:visible", false);
        });
    }
</script>
