<template>
    <Header></Header>
    <div class="max-w-7xl px-8 mx-auto my-16 space-y-12">
        <div class="grid lg:grid-cols-2">

            <!-- Text content -->
            <div>
                <h2 class="text-2xl font-medium mb-4">WHO WE ARE</h2>
                <p class="mb-4 font-regular">
                    At Caropa Couture, we redefine confidence with every stitch. Our
                    journey started with a vision to celebrate the unique beauty and
                    strength of women; we strive to offer more than just stylish apparel.
                    We believe in clothing that not only catches the eye but also lifts
                    the spirit.
                </p>
                <h2 class="text-2xl font-medium mb-4">Our Story</h2>
                <p class="mb-4 font-regular">
                    Authenticity with Style <br>
                    In the vibrant city of Miami, Florida, Caropa Couture is born under
                    the vision of Carolin Martinez. This emerging brand aims to provide
                    women with a fresh and uniquely styled option in their wardrobe,
                    emphasizing confidence and authenticity in every piece.
                </p>
                <p class="mb-4 font-regular">
                    At Caropa Couture, we deeply value the individuality and self
                    assurance of every woman. Our garments are designed for those who seek
                    to stand out and express their true selves with flair. From
                    eye-catching dresses to elegant ensembles, each item in our collection
                    enhances the beauty and confidence of our customers.
                </p>
                <p class="mb-4 font-regular">
                    Moreover, we take pride in offering unique handmade pieces crafted
                    with thread by women heads of households. These items not only convey
                    a sense of craftsmanship and quality but also provide economic
                    opportunities for these entrepreneurial women.
                </p>
                <p class="mb-4 font-regular">
                    Join us on this exciting journey of self-discovery and personal
                    expression. Discover your own unique style with Caropa Couture and be
                    part of our community that celebrates diversity and female strength.
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
            <div class="text-right">
                <div class="mb-4 flex items-center gap-2 justify-end">
                    <h2 class="text-2xl font-medium">BLUE MOM</h2>
                    <div>
                        <img src="@/assets/images/icons/heart.png" alt="Icon blue heart" class="w-4">
                    </div>
                </div>
                <p class="mb-4 font-regular">
                    At Caropa Couture, we are proud to partner with Blue Mom, an
                    organization dedicated to supporting families and friends of children
                    with autism and other conditions. Caropa Couture understands the
                    unique challenges that come with such diagnoses, offering a
                    compassionate space for support, guidance, and community.
                </p>
                <p class="mb-4 font-regular">
                    Our mission at Caropa Couture aligns with Blue Mom's values, and we
                    strive to create an inclusive, welcoming environment in our shop. We
                    believe that every child deserves a pleasant and accommodating
                    atmosphere, and we are committed to ensuring that children with autism
                    and their families feel comfortable and supported when they visit us.
                </p>
                <p class="mb-4 font-regular">
                    Together with Blue Mom, we aim to make a positive impact on the lives
                    of children with autism, providing a safe and friendly space where
                    they can feel at ease. By fostering this partnership, we hope to
                    create a supportive and understanding community for all.
                </p>
            </div>
        </div>
    </div>
    <Footer></Footer>
</template>

<script setup>
    import Header from "@/components/layouts/Header.vue";
    import Footer from "@/components/layouts/Footer.vue";
</script>
