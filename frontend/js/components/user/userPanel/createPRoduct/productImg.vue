<template>
  <div id="productImg" class="productSection">
    <div class="creatProductTitle">
      <div class="createProductTitleWrapper">
        <svg
          style="
            height: 20px;
            transform: rotate(270deg);
            margin-right: 10px;
            cursor: pointer;
          "
          @click="toggleWrapperMethod($event)"
          viewBox="0 0 100 100"
        >
          <path
            d="M 50,0 L 60,10 L 20,50 L 60,90 L 50,100 L 0,50 Z"
            class="arrow"
          ></path>
        </svg>
        <p>عکس محصول</p>
      </div>
    </div>
    <div id="productImgWrapper" class="hiddenAtDisPlay">
      <div id="images">
        <div class="increaseImgNum">
          <label for="">اضافه کردن عکس تا حداکثر ده تا</label>
          <button @click.prevent="addImgInput($event)" class="submit">
            اضافه کردن عکس
          </button>
        </div>

        <div class="allImagesWrapper">
          <!-- <single-image></single-image> -->
          <component
            @imageWasDeleted="deleteImage($event)"
            v-for="img in singleImgsArray"
            :single_id="img.id"
            :is="img.name"
          ></component>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import singleImage from "./singleImage.vue";
import { eventBus } from "../../../../userApp.js";
export default {
  components: {
    singleImage,
  },
  data() {
    return {
      imgNums: 1,
      singleImgsArray: [{ id: 1, name: "singleImage" }],
    };
  },
  created() {
    this.$on("imageWasDeleted", (id) => {
      console.log(id);
    });
  },
  watch: {
    imgNums: function (value) {
      if (value > 10) {
        this.imgNums = 10;
      }
    },
  },
  methods: {
    deleteImage(e) {
      const el = e.target;
      const wrapper = el.closest(".imagesInput");
      const shouldDelete = this.singleImgsArray.findIndex((img) => {
        return img.id == wrapper.id;
      });
      this.singleImgsArray.splice(shouldDelete, 1);
      document.getElementById(`${wrapper.id}`).remove();
    },
    addImgInput() {
      const items = document.getElementsByClassName("imagesInput");
      if (items.length >= 10) {
        return;
      }
      const randomId = this.makeid(20);
      this.singleImgsArray.push({ id:String(randomId), name: "singleImage" });
    },

    clickImage() {
      const imageInput = document.querySelector("#productImgInput");
      imageInput.click();
    },

    async showmgDetailes(img, fileDetailes) {
      const imgDetail = img.nextElementSibling;
      const imgName = imgDetail.querySelector(".imgName p"),
        imgSize = imgDetail.querySelector(".imgSize p");
      const fileName =
        fileDetailes.name.length > 15
          ? "..." + fileDetailes.name.substring(0, 11)
          : fileDetailes.name;
      imgName.innerText = fileName;
      imgSize.innerText = fileDetailes.size / 1000;
    },
    focus(e) {
      const pre = e.target.closest(".imageUrl").childNodes[0];
      pre.classList.add("blury");
    },
    blur(e) {
      const pre = e.target.closest(".imageUrl").childNodes[0];
      pre.classList.remove("blury");
    },
    makeid(length) {
      var result = "";
      var characters =
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
      var charactersLength = characters.length;
      for (var i = 0; i < length; i++) {
        result += characters.charAt(
          Math.floor(Math.random() * charactersLength)
        );
      }
      return result;
    },
  },
};
</script>

<style scoped>
#productImgWrapper > label {
  width: 100%;
  display: flex;
  justify-content: center;
}
.imgDetails:hover {
  display: block;
}
#productImg {
  padding: 10px;
}
.imgDetails p {
  font-size: 14pt;
  padding: 5px;
  width: 100px;
  overflow: hidden;
  display: flex;
  justify-content: center;
}
.imgDetails {
  position: absolute;
  left: 50%;
  top: 50px;
  display: none;
  flex-direction: column;
  justify-content: center;
  transform: translateX(-50%);
}
.imgName {
  background-color: hsla(0, 0%, 100%, 0.4);
  width: 100px;
  height: 20px;
  overflow: hidden;
  display: flex;
}
.imgName p {
  max-width: 100px;
  overflow: hidden;
  font-size: 11pt;
  text-align: left;
  white-space: nowrap;
}

#images {
  display: flex;
  width: 100%;
  margin-top: 10px;
  align-items: center;
  flex-direction: column;
  flex-wrap: wrap;
}

.allImagesWrapper {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

#productImgInput {
  display: none;
}
.increaseImgNum {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 10px 0;
}
.increaseImgNum .submit {
  margin-top: 10px;
}
@media (max-width: 850px) {
  #images {
    flex-direction: column;
    align-items: center;
  }
}
.fade-enter-active {
  animation: fadeIn 0.5s linear;
}
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
</style>
