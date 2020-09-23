<template>
    <div id="singleBlogPostItem">
            <div class="signleBlogPostItemWrapper maxIs">
                <div v-html="JSON.parse(post).content" class="postText">
                </div>
                <suggestin></suggestin>

                <comment-section :comments='JSON.parse(post).comments'></comment-section>
                <!-- <div class="comments">
                    <div class="commentsWrapper">
                        <div class="writeComment">
                            <textarea placeholder="نظر شما چیست؟" name="" id="" cols="30" rows="10"></textarea>
                            <button class='submit'>ثبت نظر</button>
                        </div>
                    </div>
                </div> -->
            </div>
    </div>
</template>

<style scoped>
    .comments{
        margin-top:50px
    }
    .commentsWrapper{
        display:flex;
        flex-direction:column;
        align-items: center;
    }
    .writeComment{
        display:flex;
        flex-direction:column;
        align-items: center;
        width:100%
    }
    .writeComment button{
        width:max-content
    }
    textarea{
        margin-bottom:20px;
        width:80%;
        height:200px;
        resize: none;
        direction:rtl;
        font-size:14pt;
        font-family:'yekan';
        box-shadow: 0 5px 30px;
    }
    #singleBlogPostItem{
        display:flex;
        margin-top:50px;    
        justify-content: center;
    }
    .signleBlogPostItemWrapper{
        width: 90%;
    }
    
    
    p{
        text-align: justify;
    }
   
</style>

<script>
    import consulate from "../consulate/consulate.vue"
    import suggestin from "./suggestin.vue"
    import commentSection from "../../user/product/commentSection.vue"
    export default {
        components:{
            consulate,
            suggestin,
            commentSection
        },
        props:['post'],
        created(){
            console.log('blog',JSON.parse(this.post))
        }
    }
</script>