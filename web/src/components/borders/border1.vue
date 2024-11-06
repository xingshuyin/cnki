<template>
    <div class="border1">
        <img src="../../assets/img//border1.png" alt="">
            <slot></slot>
    </div>
</template>
<script>
</script>
<style lang="scss" scoped>
.border1 {
    position: relative;

    img {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: none;
        /* 保持图片的原始比例，不拉伸 */
        object-position: top left;
        /* 将图片的左上角对齐到容器的左上角 */
    }
}
</style>