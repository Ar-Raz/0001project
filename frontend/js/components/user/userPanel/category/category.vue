<template>
    <div id="makeCategory">
        <div id="makeCategoryWrapper">
            <form action="">
                <category-name></category-name>
                <slicer></slicer>
                <category-variations></category-variations>
            </form>
        </div>
    </div>
</template>


<script>
import CategoryName from "./categoryName.vue"
import categoryVariations from "./categoryVariations.vue"
import slicer from "./../../template/slicer/slicer.vue"
export default {
    components:{
        CategoryName,
        categoryVariations,
        slicer
    }
}
</script>

<style scoped>
#makeCategory{
    margin-top:50px;
    display: flex;
    justify-content: center;
}
#makeCategoryWrapper{
    width: 100%;
    display: flex;
    justify-content: center;
}
form{
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}
</style>