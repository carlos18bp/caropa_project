import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("@/views/Home.vue"),
    },
    {
      path: "/product/:product_ref",
      name: "product",
      component: () => import("@/views/product/Detail.vue"),
    },
    {
      path: "/catalog",
      name: "catalog",
      component: () => import("@/views/product/Catalog.vue"),
    },
    {
      path: "/checkout",
      name: "checkout",
      component: () => import("@/views/product/Checkout.vue"),
    },
    {
      path: "/about_us",
      name: "about_us",
      component: () => import("@/views/AboutUs.vue"),
    },
  ],
});

export default router;
export const routes = router.options.routes;
