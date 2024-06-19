<template>
    <!-- Container for the image and brand information section -->
    <div class="px-72 py-16">
        <div class="flex">
            <!-- Main product image -->
            <div class="w-4/5">
                <img src="@/assets/images/product/image1.png" alt="Image 1" />
            </div>
            <!-- Brand information section -->
            <div class="flex flex-col justify-center items-center space-y-4">
                <!-- Brand logo -->
                <img src="@/assets/images/logo2.png" alt="Logo" class="w-56" />
                <!-- Brand description -->
                <p class="text-lg font-medium text-black text-center">
                    Learn more about our brand's journey, values, and commitment to quality fashion.
                </p>
                <!-- Link to About Us page -->
                <p class="text-lg font-medium text-black">
                    Discover our story |
                    <router-link :to="{ name: 'about_us' }" class="border-b-2 border-black">
                        About Us
                    </router-link>
                </p>
            </div>
        </div>
    </div>
</template>
