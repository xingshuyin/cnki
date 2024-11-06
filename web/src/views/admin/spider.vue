<!--
 * @Filename     : spider.vue
 * @Description  : wjt-前端-爬虫管理
 * @Author       : xingshuyin xingshuyin@outlook.com
 * @Date         : 2022-10-30 10:31:33
 * @LastEditors  : xingshuyin xingshuyin@outlook.com
 * @LastEditTime : 2022-11-19 22:15:04
 * Copyright (c) 2022 by Research Center of Big Data and Social Computing DARG, All Rights Reserved.
-->
<template>
    <div class="main-top">
        <div class="search">
            <!-- <f-input v-model="form.label" label="名称" /> -->
            <f-input v-model="form.name" label="名称" />
            <f-timerange v-model="special_form.range" />
        </div>
        <div class="tool">
            <el-button size="small" type="danger"
                @click="mult_delete_(`/${attrs.base_url}/mult_destroy/`, attrs?.selects, get_data)"
                v-if="attrs?.selects?.length > 0">批量删除
            </el-button>
            <el-button type="primary" v-if="attrs.can_create"
                @click="attrs.adding = true; attrs.add_form = {}; attrs.submit_type = 'add'" icon="Plus" circle />
            <f-columns-edit v-if="attrs.columns" v-model="attrs.columns" :base_url="attrs.base_url"></f-columns-edit>
            <el-button icon="Download" circle
                @click="export_data_(attrs.base_url, { create_start: special_form.range[0], create_end: special_form.range[1], ...form })" />
        </div>
    </div>
    <div class="main-table">
        <el-table :data="attrs.data" v-loading.fullscreen:false="attrs.loading" stripe border size="small"
            :expand-row-keys="attrs.expandedRowKeys" :row-key="(row) => { return row.id }"
            @selection-change="(d) => { select_(d, attrs) }" @sort-change="(d) => { sort_(d, form) }">
            <f-columns v-if="attrs.columns" v-model="attrs.columns" v-model:attrs="attrs" :callback_delete="get_data">
            </f-columns>
        </el-table>
        <t-page v-model:page="form.page" v-model:limit="form.limit" :total="attrs.total"></t-page>
    </div>
    <el-dialog v-model="attrs.adding" :title="attrs.submit_type == 'add' ? '新增' : '编辑'" width="50%" top="0" :modal="false"
        destroy-on-close style="scrollbar-width: 0;">
        <el-form :model="attrs.add_form" label-width="120px" :rules="rules" ref="form_dom">
            <el-form-item label="名称" prop="name">
                <el-input v-model="attrs.add_form.name" />
            </el-form-item>
            <el-form-item label="规则" prop="rule">
                <t-jsoneditor v-model="attrs.add_form.rule"></t-jsoneditor>
            </el-form-item>
            <el-form-item label="是否启用" prop="enable">
                <el-switch v-model="attrs.add_form.enable" />
            </el-form-item>
        </el-form>

        <template #footer>
            <span class="dialog-footer">
                <el-button @click="attrs.adding = false">取消</el-button>
                <el-button type="primary" @click="validate">
                    提交
                </el-button>
            </span>
        </template>
    </el-dialog>
</template>

<script setup>
import { get_data_, select_, mult_delete_, sort_, submit_, export_data_ } from '../../hooks/table_common'
import r from '../../utils/request';
import { spider_type } from '../../utils/data';
import store from '../../store';
store().get_userinfo().then((res) => {
    if (res.interfaces.indexOf(attrs.base_url + '-mult_update') != -1) {
        attrs.can_mult_update = true
    }
    if (res.interfaces.indexOf(attrs.base_url + '-create') != -1) {
        attrs.can_create = true
    }
})
const attrs = reactive({
    columns: [
        { type: 'text', label: '规则名称', prop: 'name', align: "left", show: true },
        { type: 'json', label: '规则', prop: 'rule', align: "left", show: true },
        { type: 'bool', label: '是否启用', prop: 'enable', align: "left", show: true },

        { type: 'text', label: '创建时间', prop: 'create_time', width: 100, align: "center", show: true },
    ],
    base_url: 'spider',
    selects: [],
    data: [],
    total: 0,
    loading: true,
    submit_type: null,
    update_item_id: null,
    adding: false,
    background: true,
    expandedRowKeys: [],
    add_form: {},
    can_create: false,
    can_mult_update: false,
})
const special_form = reactive({
    range: [undefined, undefined],
})
const form = reactive({
    page: 1,
    limit: 100,
    // defer: ['code'],  //排除字段
    // values: ['name', 'code'] //选择字段
})
watch([form, special_form], () => {
    if (special_form.range == null) {
        special_form.range = [undefined, undefined]
    }
    get_data()
})
const form_dom = ref()
const rules = reactive({  //https://element-plus.gitee.io/zh-CN/component/form.html#%E8%87%AA%E5%AE%9A%E4%B9%89%E6%A0%A1%E9%AA%8C%E8%A7%84%E5%88%99
    name: [
        { required: true, message: '请填写名称', trigger: 'blur' },
    ],
    rule: [
        { required: true, message: '请填写规则', trigger: 'blur' },
    ],
})
const validate = () => {
    form_dom.value.validate((valid, fields) => {
        if (valid) {
            submit_(attrs.base_url, attrs.add_form, attrs.submit_type, submit_success);
        } else {
            ElMessage({
                showClose: true,
                message: Object.values(fields)[0][0]['message'],
                center: true,
            });
        }
    })
}
const submit_success = (res) => {
    if (attrs.submit_type == 'add') {
        attrs.data.shift(res.data)
        attrs.add_form = {};
        attrs.adding = false
    }

    get_data()
}
const get_data = () => {
    get_data_(`/${attrs.base_url}/`, { create_start: special_form.range[0], create_end: special_form.range[1], ...form }, attrs)
}
get_data()
</script>

<style scoped lang="scss">
.detail {
    margin-left: 60px;
    margin-right: 10px;
    box-shadow: 0 0 2px 0 black;
}

:deep(.sub-table) {
    width: 100%;
    height: 200px;
}
</style>
