import vue from "vue";
import { store } from "./userStore.js";
import slicer from "./components/user/template/slicer/slicer.vue";
import footer from "./components/user/template/footer/footer.vue";
import productZoom from "./components/user/product/productZoom.vue";
import aboutUs from "./components/abouts/aboutUs.vue";
import aboutDamir from "./components/abouts/aboutDamirco.vue";
import rulesToUse from "./components/abouts/rulesToUse.vue";
import VueMeta from "vue-meta";
import { toggleDisplayAndArrow } from "./components/user/mixIns/toggleDisplayAndArrow";
import heading from "./components/user/template/header/header.vue"
import navigation from "./components/user/template/navigation/navigation.vue"
import error from "./components/user/template/error/error.vue";
vue.use(VueMeta, {
  // optional pluginOptions
  refreshOnceOnNavigation: true,
});
vue.mixin(toggleDisplayAndArrow);
import ZoomOnHover from "vue-zoom-on-hover";
vue.use(ZoomOnHover);
const app = new vue({
  el: "#app",
  components: {
    heading,
    'indexUserPanel':()=>import("./components/user/userPanel/index/index.vue"),
    'index':()=>import("./components/user/index/index.vue"),
    navigation,
    slicer,
    'createBlogPost':()=>import("./components/user/userPanel/createBlogPost/createBlogPost.vue"),
    foot: footer,
    'product':()=>import("./components/user/product/product.vue"),
    productZoom,
    'signup':()=>import("./components/user/signup/signup.vue"),
    'products':()=>import("./components/user/prodcuts/products.vue"),
    'filtering':()=>import("./components/user/prodcuts/filtering.vue"),
    'profile':()=>import("./components/user/userPanel/profile/profile.vue"),
    'category':()=>import("./components/user/category/category.vue"),
    'doneMessage':()=>import("./components/user/template/doneMessage/doneMessage.vue"),
    'blog':()=>import("./components/blog/blog/blog.vue"),
    'singleBlogPost':()=>import("./components/blog/blogPost/blogPost.vue"),
    'sellInDamir':()=>import("./components/abouts/sellInDamir.vue"),
    'buyIndamir':()=>import("./components/abouts/buyInDamir.vue"),
    aboutUs,
    aboutDamir,
    rulesToUse,
    'feedBack':()=>import("./components/user/template/feedback/feddback.vue"),
    'privacy':()=>import("./components/abouts/privacy.vue"),
    'createProduct':()=>import("./components/user/userPanel/createPRoduct/createProduct.vue"),
    'userPanelWrapper':()=>import("./components/user/userPanel/userPanelWrapper.vue"),
    'miniOrders':()=>import("./components/user/userPanel/miniOrders/miniOrders.vue"),
    'ticket':()=>import("./components/user/userPanel/ticket/ticket.vue"),
    'confirmation':()=>import("./components/user/signup/confirmation.vue"),
    'addCategory':()=>import('./components/user/userPanel/addCategory/addCategory.vue'),
    error
  },
  store,
  // Router
});

export const eventBus = new vue();
import 'swiper/swiper-bundle.css'
import "./css/reset.css";
import "./css/buttons.css";
import "./css/shared.css";
import "./css/leaflet.css";
import "./css/prettyCheckbox.css";
