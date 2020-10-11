import vue from 'vue'
import userPanelHeader from "./components/userPanel/template/userPanelHeeader/userPanelHeader.vue";
import sideMenu from "./components/userPanel/template/sideMenu/sideMenu.vue";
import userPanelWrapper from "./components/userPanel/userPanelWrapper.vue";
import Vuex from 'vuex'
vue.use(Vuex)
import {store} from "./userPanelStore"

import {toggleWrapper} from "./components/userPanel/mixIns/toggleCreateProductWrapper"
vue.mixin(toggleWrapper)
const app=new vue({
	el:"#userPanel",
	components:{
		userPanelHeader,
		sideMenu,
		userPanelWrapper,
		'index':()=>import("./components/userPanel/index/index.vue"),
		'createProduct':()=>import("./components/userPanel/createPRoduct/createProduct.vue"),
		'createBlogPost':()=>import('./components/userPanel/createBlogPost/createBlogPost.vue'),
		'addCategory':()=>import('./components/userPanel/addCategory/addCategory.vue'),
		'editVariations':()=>import("./components/userPanel/editCategoryVariations/editVariations.vue"),
		'ticket':()=>import("./components/userPanel/ticket/ticket.vue"),
		'ticketReps':()=>import("./components/userPanel/ticketReps/ticketReps.vue"),
		'myProducts':()=>import('./components/userPanel/myProducts/myProducts.vue')


	},
	store
	// Router
})
import './css/userPanelCss/shared.css'
import "./css/reset.css";
import "./css/buttons.css";