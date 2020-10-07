<template>
	<div v-if="products.length>0" class="card maxIs">
		
		<div :id="id" :class="getClass()">
			<div class="titleCard"><p>{{cardTitle}}</p></div>
			<div class="splide__track">
				<ul class="splide__list">
					<li class="splide__slide" v-for="(p,index) in products" :key="index">
						<div class="singleSlide">
							<div class="singleSlideWrapper">
								<div class="img">
									<img :src="getImage(p.product_image)" alt="">
								</div>
								<div class="descs">
									<div class="title">
										<a class="link" :href="getSlug(p.slug)">{{p.title}}</a>
									</div>
									<div class="descsP">
										<p v-html="getDescription(p.description)"></p>
									</div>
									<div class="link">
										<p>{{p.price || 0}}  تومان</p>
										<a class="submit" :href="getSlug(p.slug)">مشاهده</a>
										
									</div>
								</div>
							</div>
						</div>
					
					</li>
				</ul>
			</div>
		</div>
	</div>
</template>
<script>	
    export default{
		props:['products','cardTitle',"id"],
		data(){
			return{
				container:null,
				isDown:false,
				startX:null,
				scrollLeft:null,
				glide:null
			}
		},
		data(){
			return{
				perShow:2
			}
		},
		mounted(){
			this.container=document.querySelector('.cardWrapper');
			let per=this.reCalculatePer()
			const glide=new Splide( `#${this.id}`,{
					type   : 'loop',
					perPage: per,
					perMove: 1,
				} );
				glide.mount()
				window.addEventListener("resize",()=>{
					let pper=this.reCalculatePer()
					glide.options.perPage=pper
				})
				console.log('from card',this.products)
		},
        methods:{
			getDescription(desc){
				return desc.length>130 ? desc.substring(0,130)+"...." : desc
			},
			getSlug(slug){
				return `/products/product-detial/${slug}`
			},
			reCalculatePer(){
				let per=2
					let width=window.innerWidth
					if(width>=1100){
						per=4
					}
					else if(width<=1099 && width>=851){
						per=3
					}else if(width<=850 && width>=600){
						per=2
					}else if(width<=599){
						per=1
					}
					return per
					
			},
            getUrl(p){
                return p.url
            },
            getDesc(desc){
                console.log(desc.substring(0,30).length)
                return desc.length>30 ? desc.substring(0,100)+"..." : desc
			},
			getImage(img){
				console.log(img)
				return img
			},
			getClass(){
				return `splide ${this.id}`
			}
		}
    }
	
</script>



<style scoped>
.titleCard p{
	font-size:24px;
	font-weight: 100;
	margin:10px;
}
	.card{
		box-shadow: 0px 2px 5px 0 rgba(0,0,0,0.2);
		background:#ffffff;
		margin-top:50px;
        overflow: auto;
        width:100%;
		position: relative;
		display: flex;
		/* align-items: flex-end; */
		flex-direction: column;
    }
	
	img{
		width: 250px;
		height: 230px;
		border-top-left-radius: 10px;
		border-top-right-radius: 10px;
	}
	.singleSlide{
		width:280px;
		padding:5px;
		margin-top:10px;
	}
	.link{
		display: flex;
    justify-content: space-between;
    align-items: center;
    direction: rtl;
    text-align: right;
    height: 70px;
	}
	.singleSlide img{
		width:280;
	}
	.img{
		display:flex;
		justify-content: center;
	}
	.singleSlide .descsP{
		height:120px;
	}
	.descsP p{
		color:#707070;
		font-weight:bold
	}

	.title{
		margin-top:5px;
		margin-bottom:5px;
		display:flex;
		justify-content: flex-end;
	}
	.splide--draggable>.splide__track>.splide__list>.splide__slide {
    -webkit-user-select: none;
    user-select: none;
    display: flex;
	justify-content: center;
	margin-top:20px;
	margin-bottom:10px
}
.splide__track{
	margin-top:20px
}
.splide__slide{
  padding:10px;
}
</style>