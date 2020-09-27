<template>
    <div id="selectCategory">
        <div id="selectCategoryWrapper">
            <div class="headCategory cats">
                <label for="">دسته بندی محصول را انتخاب کنید</label>
                <input placeholder="جست و جو..." list="browsers" autocomplete="off" name="category">
                <datalist id="browsers">
                    <option v-for='cat in getHeadCats' :key='ket.id' :value="cat.title"></option>
                </datalist>
            </div>
            <div class="subCats cats">
                <label for="">زیر دسته را انتخاب کنید</label>
                <input placeholder="جست و جو..." list="browsers" autocomplete="off" name="category">
                <datalist id="browsers">
                    <option value="دسته 1"></option>
                </datalist>
            </div>
        </div>
    </div>
</template>
<style scoped>
    input{
        color:black;
        direction:rtl;
        border:1px solid rgb(210,214,222);
        padding:10px
    }

    #selectCategory{
        margin-top:20px;
        margin-bottom:20px;
        width:100%
    }
    #selectCategoryWrapper{
        display:flex;
        flex-direction:column;
        align-items: center;
    }
    label{
            margin-bottom:10px
        }
    label:before{
        content:"* ";
        color:red;
        font-size:20pt;
        font-weight: 900;
    }
    @media (max-width: 500px)
    {
        #selectCategoryWrapper{
            display:flex;
            flex-direction:column;
            align-items: center;
        }
        
        #selectCategoryWrapper input,#selectCategoryWrapper datalist{
            width:90%
        }

    }
    @media (max-width:320px)
    {
        #selectCategoryWrapper label{
            font-size:15pt
        }
    }
</style>

<script>
    // import vSelect from 'vue-select'
    import axios from "axios"
export default {
    data(){
        return{
            options:['Canada', 'United States'],
            allCats:null
        }
    },
    computed:{
        getHeadCats(){
            console.log("getAllCars",this.allCats)
            return this.allCats
        }
    },
    mounted(){
        let {data}=axios.get("/categories-api/list")
        console.log("axios get",data)
        this.allCats=data


    }

}
</script>