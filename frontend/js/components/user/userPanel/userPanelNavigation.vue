<template>
    <div  id='userPanelNavigation' @click='toggleUserPanelNavigation(),toggleBodyOverFlow()'>
        <div id="userPanelNavigationWrapper" @click='prevent($event)'>
            <ul>
                <li><a class="href" href="/userPanel/indexx">داشبورد</a> </li>
                <li><a class="href" href="/create">اضافه کردن محصول برای فروش</a></li>
                <li><a class="href" href="/category">اضافه کردن دسته بندی</a></li>
                <li><a class="href" href="/blogpost">اضافه کردن پست بلاگ</a></li>

            </ul>
        </div>
    </div>
</template>


<script>
    import {mapActions} from 'vuex'
    import {toggleBodyOverFlow} from "../mixIns/toggleBodyOverFlow"
	import {adjustElFromTop} from '../mixIns/adjustElFromTop.js'
    export default{
        name:"userPanelNavigation",
        mixins:[toggleBodyOverFlow,adjustElFromTop],
        methods:{
            ...mapActions([

                'toggleUserPanelNavigation',
                'swapUserPanelComponent'
            ]),
          go(e){
            // window.navigator.hr
          },
             prevent(e){
               if(e.target.classList.contains("href")){
                 const href=e.target.getAttribute("href")
                 window.location.href = window.location.host+"/"+href;
                 return
               }
                e.stopPropagation();
                e.preventDefault();

            },
          toggleUserPanelNavigation(){
              this.$emit("close")
          }

        },
        mounted(){
            this.adjustFromTop(document.querySelector("#userPanelNavigationWrapper"))
		    this.toggleBodyOverFlow('hidden') 
        }
    }
</script>


<style scoped>
    ul{
        width:100%;
    }
    #userPanelNavigation{
        position:absolute;
        z-index:667;
        top:0;
        left:0;
        bottom:0;
        right:0;
        width:100%;
        height:100%;
        background: rgba(0,0,0,0.4);
    }
    #userPanelNavigationWrapper{
        background:#f6f6f4;
        position:absolute;
        right:0;
        top:0;
        bottom:0;
        max-width:80%;
        height:100vh
    }
    ul{
        display:flex;
        flex-direction:column;
        align-items: flex-end;
    }
    ul li{
        padding:10px;
        display:flex;
        align-items: center;
        justify-content: flex-end;
        text-align: right;
        width:100%;
        border-bottom:1px solid rgb(206, 187, 187)
    }
    ul li a{
        padding:5px;
        color:black;
    }
    .icon{
        width:30px;
        height:30px
    }

</style>