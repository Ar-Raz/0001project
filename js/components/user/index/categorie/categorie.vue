<template>
    <div id="sideSliderCats">
        <div id="sideSlidesCatsWrapper">
            <!-- <div id="hamCats">
                <ham></ham>
                دسته بندی
            </div> -->
            <div id="allCats">
                <ul>
                    <template v-for="(c,i) in mainCats">
                        <li v-if="i<11"  class="parentLi"><arrow></arrow>  {{c.title}} 
                            <div class="sideSliderSubmenu">
                                <div class="subTitleWrapper">
                                    <div class="SubTitle"><p>{{c.title}}</p></div>
                                    <ul>
                                        <li v-if="subI<=5" v-for="(sub,subI) in c.subs"><a :href="getUrl(sub.title)">{{sub.title}}</a></li>
                                    </ul>
                                </div>
                            </div>
                        </li>
                    </template>
                    
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
    import arrow from "../../template/arrow/arrow.vue"
    import ham from "../../template/hamIcon/ham.vue"
    export default{
        components:{
            ham,
            arrow
        },
        props:['mainCats'],
        created(){
            console.log("cats",this.mainCats)
        },
        methods:{
            getUrl(url){
                return `/categories/${url}`
            }
        }
    }
</script>


<style scoped>
    ul li:hover .sideSliderSubmenu{
        display:block;
        animation:fadeIn 0.2s linear
    }
    @keyframes fadeIn{
        from{
            opacity:0
        }
        to{
            opacity:1;
        } 
    }
    ul li:hover{
        border-top:1px solid rgb(129, 129, 129);
        border-bottom:1px solid rgb(129, 129, 129);
    }
    ul li{
        text-align: right;
    }
    .sideSliderSubmenu{
        position: absolute;
        display:none;
        right:100%;
        z-index:667;
        background-color: white;
        height:max-content;
        top:-20px;
        width:300px;
        border-left:1px solid rgb(223, 223, 223);
        background: #ffffff
    }
    .subTitleWrapper{
        display:flex;
        flex-direction:column;
        align-items: flex-end;
        padding:10px
    }
    .subtitle{
        font-size:20pt;
    }
    .sideSliderSubmenu ul li a{
        font-size:12pt;
        color:rgb(71, 71, 245) !important
    }
    .arrow{
        width:20px;
        height:20px;   
    }
    #sideSlidesCatsWrapper{
        width:100%;
        padding:10px;
    }

    #sideSliderCats{
        display:flex;
        justify-content: flex-start;
        width:240px;
    }
    ul{
        width:100%
    }
    ul>li{
        line-height: 2rem;
        width:100%;
        display:flex;
        justify-content: space-between;
    }
    .sideSliderSubmenu li{
        display:flex;
        justify-content:flex-end
    }
    .parentLi{
        position: relative;
        font-size:14px;
        cursor: pointer;
        text-align: right;
    }
    .parentLi:hover .sideSliderSubmenu{
        display:block
    }
    #hamCats{
        display:flex;
        align-items:center
    }
    @media (max-width:801px)
	{
		#sideSliderCats{
			display:none
		}
	}
    .seeMore{
        display:flex;
        justify-content: flex-end
    }

</style>

