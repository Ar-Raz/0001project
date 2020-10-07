<template>
  <div id="createProduct" class="maxIs">
    <div id="createProductWrapper">
      <form action="" method="post">
        <select-category :cats="JSON.parse(cats)"></select-category>
        <div id="name" class="productSection">
          <div id="nameWrapper">
            <label for="">نام محصول:</label>
            <input type="text" placeholder="نام" name="product-title" />
          </div>
        </div>
        <slicer></slicer>
        <main-picture></main-picture>
        <slicer></slicer>
        <product-img></product-img>

        <slicer></slicer>

        <product-descs></product-descs>
        <slicer></slicer>
        <short-description></short-description>

        <slicer></slicer>
        <aditional-information></aditional-information>
        <slicer></slicer>
        <variations></variations>

        <button type="submit" class="submit">ثبت محصول</button>
      </form>
    </div>
  </div>
</template>

<style scoped>
#createProduct {
  display: flex;
  justify-content: center;
  width: 100%;
}
#nameWrapper label:before {
  content: " * ";
  color: red;
  font-size: 20pt;
  font-weight: 900;
}
form {
  width: 100%;
}
#createProductWrapper {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
#createProductWrapper form {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.productSection {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

#nameWrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
#nameWrapper input {
  width: 200px;
}
#nameWrapper label {
  margin-bottom: 10px;
}

input[type="text"] {
  color: black;

  width: 30%;
  padding: 10px;
}
input {
  border: 1px solid rgb(210, 214, 222);
}

.orderInput input {
  width: 100%;
}
.submit {
  margin-top: 20px;
  margin-bottom: 20px;
}

.title p,
#productDescsWrapper label {
  color: #0061af;
  font-size: 17pt;
  font-weight: lighter;
}
label {
  display: flex;
}
@media (max-width: 500px) {
  #nameWrapper {
    display: flex;
    flex-direction: column;
  }
  #createProduct
  {
    width: 100%;
  }
  .userPanelComp{
    border:0
  }
  #nameWrapper input {
    width: 90%;
  }
}
</style>

<script>
import slicer from "../../template/slicer/slicer.vue";
import Editor from "@tinymce/tinymce-vue";
import productImg from "./productImg.vue";
import productDescs from "./productDescs.vue";
import aditionalInformation from "./aditionalInformation.vue";
import selectCategory from "./selectCategory.vue";
import variations from "./variations.vue";
import shortDescription from "./shortDescription.vue";
import mainPicture from "./mainPicture.vue";
export default {
  components: {
    editor: Editor,
    shortDescription,
    slicer,
    selectCategory,
    productImg,
    productDescs,
    aditionalInformation,
    variations,
    mainPicture
  },

  props: ["cats",'products'],
  created() {
    console.log("products",JSON.parse(this.products))
    var scriptTag = document.createElement("script");
    scriptTag.src =
      "https://cdn.datatables.net/v/dt/dt-1.10.16/sl-1.2.5/datatables.min.js";
    scriptTag.id = "my-datatable";
    document.getElementsByTagName("head")[0].appendChild(scriptTag);
  },
};
</script>
