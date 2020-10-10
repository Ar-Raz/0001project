<template>
  <div id="productDescs" class="productSection">
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
        <p>توضیحات محصول</p>
      </div>
    </div>
    <div id="productDescsWrapper" class="hiddenAtDisPlay">
      <br />
      <textarea id="editor" name="product-description"></textarea>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    init() {
      tinymce.init({
        setup: function (editor) {
          /* example, adding a group toolbar button */
          editor.ui.registry.addGroupToolbarButton("alignment", {
            icon: "align-left",
            tooltip: "Alignment",
            items: "alignleft aligncenter alignright | alignjustify",
          });
        },
        language: "fa",
        selector: "#editor",
        plugins: "image code table lists link",
        toolbar:
          "undo redo | link image | code fontsizeselect forecolor backcolor numlist bullist alignment bold",
        menubar: "table",
        fontsize_formats: "11px 12px 14px 16px 18px 24px 36px 48px",
        width: "100%",
        height:'600px',
        images_upload_url: "test/",
        image_title: true,
        automatic_uploads: true,
        file_picker_types: "image",
        file_picker_callback: function (cb, value, meta) {
          var input = document.createElement("input");
          input.setAttribute("type", "file");
          input.setAttribute("accept", "image/*");

          input.onchange = function () {
            var file = this.files[0];

            var reader = new FileReader();
            reader.onload = function () {
              var id = "blobid" + new Date().getTime();
              var blobCache = tinymce.activeEditor.editorUpload.blobCache;
              var base64 = reader.result.split(",")[1];
              var blobInfo = blobCache.create(id, file, base64);
              blobCache.add(blobInfo);

              cb(blobInfo.blobUri(), { title: file.name });
            };
            reader.readAsDataURL(file);
          };

          input.click();
        },
        images_upload_handler: function (blobInfo, success, failure, progress) {
          var xhr, formData;

          xhr = new XMLHttpRequest();
          xhr.withCredentials = false;
          xhr.open("POST", "/test/");

          xhr.upload.onprogress = function (e) {
            progress((e.loaded / e.total) * 100);
          };

          xhr.onload = function () {
            var json;

            if (xhr.status < 200 || xhr.status >= 300) {
              failure("HTTP Error: " + xhr.status);
              return;
            }

            json = JSON.parse(xhr.responseText);

            if (!json || typeof json.location != "string") {
              failure("Invalid JSON: " + xhr.responseText);
              return;
            }

            success(json.location);
          };

          xhr.onerror = function () {
            failure(
              "Image upload failed due to a XHR Transport error. Code: " +
                xhr.status
            );
          };

          formData = new FormData();
          formData.append("file", blobInfo.blob(), blobInfo.filename());

          xhr.send(formData);
        },
        content_style:
          "body { font-family:Helvetica,Arial,sans-serif; font-size:14px }",
      });
    },
    mounted() {
      this.init();
    },
  },

  mounted() {
    this.init();
  },
};
</script>

<style scoped>
#productDescs {
  padding: 10px;
}
label {
  color: #0061af;
  font-size: 17pt;
  font-weight: lighter;
}
#productDescsWrapper {
  padding: 10px;
  width: 100%;
  align-items: flex-end;
}
#productDescs textarea {
  width: 100%;
  height: 500px;
  padding: 10px;
}
@media (max-width: 500px) {
  #productDescsWrapper{
    padding: 0;
  }

}
</style>
