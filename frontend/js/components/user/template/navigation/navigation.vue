<template>
  <div id="navigation">
    <div class="naviagtionWrapper">
		<div class="hamIcon">
			<div class="sikhWrapper" @click="toggleNavigation($event)">
				<div @click="toggleNavigation($event)" class="sikh1 sikh"></div>
				<div @click="toggleNavigation($event)" class="sikh2 sikh"></div>
				<div @click="toggleNavigation($event)" class="sikh3 sikh"></div>
			</div>
			<transition name="fade" mode="out-in">
				<ul v-if="showNavigation">
					<li><a href="/">خانه</a></li>
					<li><a href="#">درباره ما</a></li>
					<li><a href="/blog/posts/">وبلاگ</a></li>
					<li @click="toggleSubMenu()">دسته بندی محصولات</li>
				</ul>
			</transition>
		
		</div>

		
	</div>
    <!-- <transition name='toggleSubMenu' mode='out-in'> -->
    <flat-menu v-if="isSubMenuOpen"></flat-menu>
    <!-- </transition> -->
  </div>
</template>

<script>
import ham from "../hamIcon/ham.vue";
import slicer from "../slicer/slicer.vue";
import flatMenu from "../flatMenu/flatMenu.vue";
import { mapGetters } from 'vuex'
import { mapActions } from "vuex";

export default {
  components: {
    flatMenu,
  },
  computed: {
	  ...mapGetters([
		  'isSubMenu'
	  ]),
	  isSubMenuOpen(){
		  console.log('comp',this.isSubMenu)
		  return this.isSubMenu
	  }
  },
  data(){
	  return{
		  showNavigation:false
	  }
  },
  mounted(){
	  window.addEventListener("resize",this.checkNavigation)
	  this.checkNavigation()
  },
  methods:{
	  checkNavigation(){

		if(window.innerWidth>450){
		  this.showNavigation=true
		}else{
			this.showNavigation=false
		}
		this.changeSikhStyles()
	},
	toggleSubMenu(){
		this.$store.dispatch("toggleSubMenu")
		console.log(this.$store.state.catsWithSubs,"hey")
	},
	toggleNavigation(e){
		e.stopPropagation()
	  	e.preventDefault()
		this.showNavigation=!this.showNavigation
		this.changeSikhStyles()
	},
	changeSikhStyles(){
		const sikh1=document.querySelector(".sikh1")
		const sikh2=document.querySelector(".sikh2")
		const sikh3=document.querySelector(".sikh3")
		const wrapper=document.querySelector(".sikhWrapper")
		if(this.showNavigation){
			sikh2.style.transform="rotate(135deg) translate(-6px, 7px)"
			sikh1.style.transform="rotate(-135deg) translate(-4px,-4px)"
			sikh2.style.webkitTransform ="rotate(135deg) translate(-6px, 7px)"
			sikh1.style.webkitTransform ="rotate(-135deg)translate(-4px,-4px)"
			sikh3.style.display="none"
			// wrapper.style.marginTop="5px"
		}else{
			wrapper.style.marginTop="0"
			sikh3.style.display="block"
			sikh2.style.transform="rotate(0) translate(0, 0)"
			sikh1.style.transform="rotate(0)"
			sikh2.style.webkitTransform ="rotate(0) translate(0, 0)"
			sikh1.style.webkitTransform ="rotate(0)"
		}
	}
  }
};
</script>
<style scoped>
.hamIcon{
	position: relative;
	height:50px;
	border-bottom:1px solid #d9d9d8;
	border-top:1px solid #d9d9d8;
}
.sikhWrapper{
	display:none;
	
}
ul{
	background:#f6f6f4;
	display:flex;
	justify-content: flex-end;
	width:100%;
}
li{
	margin:10px
}
.sikh1{
	width:40px;
	height:4px;
	border-radius:5px;
	position:relative;
	transition:all 0.4s
}
.sikh2{
	width:40px;
	height:4px;
	border-radius:5px;
	transition:all 0.4s
}
.sikh3{
	width:40px;
	height:4px;
	border-radius:5px;
	position:relative;
}
.sikh{
	background:#096fd3;
}
@media (max-width:450px){
	.hamIcon{
		display:flex;
		flex-direction:column;
		align-items:center	;
		position:relative;
		justify-content: center;
	}
	ul{
		position:absolute;
		top:100%;
		display:flex;
		flex-direction:column;
		align-items:center;
		background:#251f1f;
		z-index:6;
	}
	li{
		color:white;
	}
	a{
		color:white;
	}
	.sikhWrapper{
		display: flex;
		flex-direction: column;
		justify-content: space-evenly;
		height:40px;
	}
}
</style>