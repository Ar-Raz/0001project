import vue from "vue";
import { store } from "./userStore.js";
import heading from "./components/user/template/header/header.vue";
import index from "./components/user/index/index.vue";
import navigation from "./components/user/template/navigation/navigation.vue";
import slicer from "./components/user/template/slicer/slicer.vue";
import footer from "./components/user/template/footer/footer.vue";
import product from "./components/user/product/product.vue";
import productZoom from "./components/user/product/productZoom.vue";
import signup from "./components/user/signup/signup.vue";
import products from "./components/user/prodcuts/products.vue";
import filtering from "./components/user/prodcuts/filtering.vue";
import userPanel from "./components/user/userPanel/userPanel.vue";
import category from "./components/user/category/category.vue";
import doneMessage from "./components/user/template/doneMessage/doneMessage.vue";
import blog from "./components/blog/blog/blog.vue";
import singleBlogPost from "./components/blog/blogPost/blogPost.vue";
import sellInDamir from "./components/abouts/sellInDamir.vue";
import buyIndamir from "./components/abouts/buyInDamir.vue";
import aboutUs from "./components/abouts/aboutUs.vue";
import aboutDamir from "./components/abouts/aboutDamirco.vue";
import rulesToUse from "./components/abouts/rulesToUse.vue";
import privacy from "./components/abouts/privacy.vue";
import feedBack from "./components/user/template/feedback/feddback.vue";
import VueMeta from "vue-meta";
import createProduct from "./components/user/userPanel/createPRoduct/createProduct.vue";
import { toggleDisplayAndArrow } from "./components/user/mixIns/toggleDisplayAndArrow";

vue.use(VueMeta, {
  // optional pluginOptions
  refreshOnceOnNavigation: true,
});
vue.mixin(toggleDisplayAndArrow);
import { routes } from "./routes.js";
import ZoomOnHover from "vue-zoom-on-hover";
vue.use(ZoomOnHover);
const app = new vue({
  el: "#app",
  components: {
    heading,
    index,
    navigation,
    slicer,
    foot: footer,
    product,
    productZoom,
    signup,
    products,
    filtering,
    userPanel,
    category,
    doneMessage,
    blog,
    singleBlogPost,
    sellInDamir,
    buyIndamir,
    aboutUs,
    aboutDamir,
    rulesToUse,
    feedBack,
    privacy,
    createProduct,
  },
  store,
  // Router
});

export const eventBus = new vue();

import "./css/reset.css";
import "./css/buttons.css";
import "./css/shared.css";
import "./css/leaflet.css";
import "./css/prettyCheckbox.css";
