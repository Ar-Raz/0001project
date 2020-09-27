<template>

        <div id='productImg' class='productSection'>
                    <div id="productImgWrapper">
                        <label for="productImgInput">
                            عکس محصول را وارد کنید
                        </label>
                        <div id="images">
                            <div class="increaseImgNum">
                                <label for="">اضافه کردن عکس تا حداکثر ده تا</label>
                                <button @click.prevent='addImgInput($event)' class="submit">اضافه کردن عکس</button>
                            </div>


                            <div class="allImagesWrapper">
                                
                                    <!-- <single-image></single-image> -->
                                <component @imageWasDeleted="deleteImage($event)" v-for="img in singleImgsArray" :key='img.id' :id="img.id" :is="img.name"></component>
                                
                            </div>
                        </div>
                    </div>
                </div>
</template>
<script>
    import singleImage from "./singleImage.vue"
    import {eventBus} from "../../../../userApp.js"
export default {
    components:{
        singleImage
    },
    data(){
        return{
            imgNums:1,
            singleImgsArray:[{id:1,name:"singleImage"}]
        }
    },
    created(){
        this.$on("imageWasDeleted",id=>{
            console.log(id)
        })
    },
    watch:{
        imgNums:function(value){
            if(value>10)
            {
                this.imgNums=10
            }
        }
    },
    methods:{
        deleteImage(e){
            const el=e.target
            const wrapper=el.closest(".imagesInput")
            const shouldDelete=this.singleImgsArray.findIndex(img=>{
                return img.id==wrapper.id
            })
            this.singleImgsArray.splice(shouldDelete,1)
            document.getElementById(`${wrapper.id}`).remove()
        },
        addImgInput(){
            const items=document.getElementsByClassName('imagesInput')
            if(items.length>=10){
                return
            }
            const randomId=this.makeid(20)
            this.singleImgsArray.push({id:randomId,name:'singleImage'})
            
        },
        
        clickImage(){
                const imageInput=document.querySelector("#productImgInput")
                imageInput.click()
        },
        
        async showmgDetailes(img,fileDetailes)
        {
            const imgDetail=img.nextElementSibling
            const imgName=imgDetail.querySelector(".imgName p"),
                  imgSize=imgDetail.querySelector(".imgSize p");
            const fileName=fileDetailes.name.length>15 ? '...'+fileDetailes.name.substring(0,11)  : fileDetailes.name
            imgName.innerText=fileName
            imgSize.innerText=(fileDetailes.size)/1000
        }
        ,
        focus(e){
            const pre=e.target.closest(".imageUrl").childNodes[0]
            pre.classList.add('blury')
        },
        blur(e){
            const pre=e.target.closest(".imageUrl").childNodes[0]
            pre.classList.remove('blury')
        },
        makeid(length) {
           var result           = '';
           var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
           var charactersLength = characters.length;
           for ( var i = 0; i < length; i++ ) {
              result += characters.charAt(Math.floor(Math.random() * charactersLength));
           }
           return result;
        }
    }
}
</script>

<style>
    
    
    #productImgWrapper{
        display:flex;
        flex-direction:column
    }
    #productImgWrapper > label{
        width:100%;
        display:flex;
        justify-content: center;
    }
    .imgDetails:hover{
        display:block
    }
    .imgDetails p{
        font-size:14pt;
        padding:5px;
        width:100px;
        overflow: hidden;
        display:flex;
        justify-content: center;
    }
    .imgDetails{
        position: absolute;
        left:50%;
        top:50px;
        display: none;
        flex-direction:column;
        justify-content: center;
        transform: translateX(-50%);
    }
    .imgName{
        background-color: hsla(0,0%,100%,.4);;
        width: 100px;
        height:20px;
        overflow: hidden;
        display: flex;
        }
    .imgName p{
        max-width:100px;
        overflow: hidden;
        font-size:11pt;
        text-align: left;
        white-space: nowrap;;
    }
    .uploadImage{
        display:flex;
        align-items: center;
    }
    .imageUrl img{
        display:none;
        width:120px;
        height:120px;
        border-radius: 20px;
    }
    .imageUrl img:hover{
        -webkit-filter: blur(8px);
        -moz-filter: blur(8px);
        -o-filter: blur(8px);
        -ms-filter: blur(8px);
        filter: blur(8px);
    }
    .blury{
        -webkit-filter: blur(8px);
        -moz-filter: blur(8px);
        -o-filter: blur(8px);
        -ms-filter: blur(8px);
        filter: blur(8px);
    }
    
    #images{
        display: flex;
        width:100%;
        margin-top:10px;
        align-items: center;
        flex-direction:column;
        flex-wrap: wrap;
    }
    
    .allImagesWrapper{
        display:flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }
    
    #productImgInput
    {
        display:none
    }
    .increaseImgNum{
        display:flex;
        flex-direction: column;
        align-items: center;
        margin:10px 0;
    }
    .increaseImgNum .submit{
        margin-top:10px;
    }
    @media (max-width:850px)
    {
        #images{
            flex-direction: column;
            align-items: center;
        }
    }
    .fade-enter-active{
        animation:fadeIn .5s linear
    }
    @keyframes fadeIn {
        from{
            opacity:0;
        }
        to{
            opacity:1
        }
    }
</style>