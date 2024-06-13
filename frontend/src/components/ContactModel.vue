<template>
  <div
    id="contact_modal"
    tabindex="-1"
    aria-hidden="true"
    class="fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full">
    <div class="relative w-1/3">

      <!-- Modal content -->
      <div class="relative bg-white rounded-lg shadow">

        <!-- Modal header -->
        <div class="flex items-start justify-between p-5 pb-0">
          <h3 class="text-xl font-semibold text-gray-900 lg:text-2xl">
            Get In Touch
          </h3>
          <button
            id="closeButton"
            data-modal-hide="contact_modal"
            type="button"
            class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center"
          >
            <svg
              class="w-5 h-5"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                clip-rule="evenodd"
              ></path>
            </svg>
          </button>
        </div>

        <!-- Modal body -->
        <div class="p-6">
          <div class="flex items-center pb-4">
            <div class="flex items-center w-8">
              <img src="@/assets/images/icons/phone_call.png" class="size-6" />
            </div>
            <a href="tel:+17543999909" class="text-xl pl-2"
              >+1 (754) 399-9909</a
            >
          </div>
          <div class="flex items-center pb-4">
            <div class="flex items-center w-8">
              <img src="@/assets/images/icons/sharp_email.png" class="size-6" />
            </div>
            <a href="mailto:info@caropacouture.com" class="text-xl pl-2"
              >info@caropacouture.com</a
            >
          </div>
          <div class="flex items-center">
            <div class="flex items-center w-8">
              <img src="@/assets/images/icons/location.png" class="size-6" />
            </div>
            <p class="text-xl pl-2">
              9620 Stirling RD Unit 4-103 Cooper City, Fl 33024
            </p>
          </div>
        </div>

        <!-- Map Container 
        <div class="w-full h-40">
          <GoogleMap
            api-key="AIzaSyD7cf5pD4u32w9k2zEnjq19nd8WlGmm-ls"
            class="h-full"
            :center="center"
            :zoom="10"
          >
            <Marker :options="{ position: center }" />
          </GoogleMap>z
        </div>
        -->
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
  </div>
</template>

<script setup>
  import { initModals } from "flowbite";
  import { onMounted } from "vue";
  import { GoogleMap, Marker } from "vue3-google-map";

  /**
   * Fetch the list of products from the store when the component is mounted.
   */
  onMounted(() => {
    initModals();
  });
</script>
