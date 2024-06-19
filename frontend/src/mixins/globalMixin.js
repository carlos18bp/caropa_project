import { useProductStore } from '@/stores/product';

export default {
  data() {
    return {
      globalState: 'This is a global state',
    };
  },
  created() {
    const productStore = useProductStore();
    const storedCartProducts = localStorage.getItem('cartProducts');

    // Load cart products from local storage or initialize to an empty array
    productStore.cartProducts = storedCartProducts ? JSON.parse(storedCartProducts) : [];
  },
  methods: {
    /**
     * Global method to log a message to the console
     */
    globalMethod() {
      console.log('This is a global method');
    },
  },
};
