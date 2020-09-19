<template>
	<div id="flatMenu" @click="toggleSubMenu(),toggleOverFlow()">
		<div id="flatMenuWrapper" @click='prevent'>
			<ul>
			    <li class="parentLi" v-for="(item,i) in getCats" :key="i">


			    	<div class="link" @click="openMySubMenu($event)">
			    		
			    		<svg viewBox="0 0 100 100"><path d="M 50,0 L 60,10 L 20,50 L 60,90 L 50,100 L 0,50 Z" class="arrow" transform="rotate(180deg)"></path></svg>
			    		<p>{{item.title}}</p>
			    	</div>
			    	

			    	<ul class="subMenu">
			    		<li v-for="(subs,ind) in item.sub_category_of" :key="ind" class="prog"><a class="prog" :href="getHref(sub_category_of.title)">{{sub_category_of.title}}</a></li>
			    	</ul>


			    </li>
				
			</ul>
		</div>
	</div>
</template>

<style scoped>
	#flatMenu{
		position: absolute;
		width:100%;
		top:0;
		bottom:0;
		background:rgba(0,0,0,0.5);
		z-index:669
	}
	#flatMenuWrapper{
		position:absolute;
		width:max-content;
		background:#f6f6f4;
		/* height:100vh; */
		height: 100%;
		z-index:670;
		right:-100%;
		width:max-content;
		transition: all 1s;
		overflow: auto;

	}
	.openWrapper{

	}
	ul{
		padding:10px;
		line-height: 2rem;
		overflow: auto;
		height:100vh
	}
	li{
		text-align: right;
		position:relative;
		margin-top: 5px;
		margin-bottom: 5px
	}
	.subMenu{
		background-color: #dfdfdf;
		width:100%;
		padding:0;
		height:0;
		transition: all 0.4s;
		overflow: hidden;
	}
	.subMenu li{
		padding:5px;
	}
	svg{
		width:15px;
		height: 15px;
		transform: rotate(-90deg);
		margin-right: 20px
	}
	.link{
		display: flex;
    	justify-content: space-between;
    	align-items: center;
    	cursor:pointer;
	}


</style>

<script>
	import {mapActions} from "vuex"
	import {toggleBodyOverFlow} from "../../mixIns/toggleBodyOverFlow.js"
	import {adjustElFromTop} from '../../mixIns/adjustElFromTop.js'
	import axios from "axios"
	export default{
		mixins:[toggleBodyOverFlow,adjustElFromTop],
		methods:{
			...mapActions([
				'toggleSubMenu'
			]),
			prevent(e){
				// if(!e.target.classList.contains("prog"))
				// {
					e.stopPropagation();
					e.preventDefault();
				//}
				
				
				
			},
			toggleOverFlow(){
	
				this.toggleBodyOverFlow()
			},
			openMySubMenu(e){
				let next
				const parentEl=e.target.closest(".parentLi")
				const scg=parentEl.querySelector("svg")
				next=parentEl.childNodes[2]

				next.style.transition = "all 0.5s ease-in-out";

				
				
				const allSubs=document.querySelectorAll('.subMenu')
				const height = getComputedStyle(next).height
				if(height!="0px"){
					next.style.height = '0px'
					return
				}
				allSubs.forEach( sub=>{
					sub.style.height='0px'
				});
				if(height=="0px"){
					next.style.height  =`${(next.querySelectorAll('li').length)*52}px`
				}else{
					next.style.height = '0px'
				}
				
				
			},
			rotateArrow(el){
				el.style.transition = 'all 0.5s ease-in-out'
				el.style.transform="rotate(180deg)"
			},
			getHref(title){
				return `/categories/${title}`
			}

		},
		async mounted(){
			const menuWrapper=document.querySelector("#flatMenuWrapper")
			this.adjustFromTop(menuWrapper,false)
			this.toggleBodyOverFlow('hidden')
			menuWrapper.style.right="0"
			this.cats=this.$store.getters.getCatsWithSubs
			console.log(this.cats)

			

		},
		data(){
			return {
				cats:null
			}
		},
		computed:{
			getCats(){
				// return this.cats
				console.log(this.$store.getters.getCatsWithSubs)
				return this.$store.getters.getCatsWithSubs
			}
		}
		
		
	}


</script>