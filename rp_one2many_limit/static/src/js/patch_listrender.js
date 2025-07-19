/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { ListRenderer } from "@web/views/list/list_renderer";
import { useState,Component, onWillStart } from "@odoo/owl";
import { rpc } from "@web/core/network/rpc";

patch(ListRenderer.prototype, {
  setup() { 
    super.setup(...arguments);
    onWillStart(async ()=>{
      const field_type = this.props.activeActions.type;
      const field_name = this.props.nestedKeyOptionalFieldsData?.field;
      const field_model = this.props.nestedKeyOptionalFieldsData?.model;
      // console.log(": ListRenderer setup field_type : ",field_type);
      // console.log(": ListRenderer setup field_name : ",field_name);
      // console.log(": ListRenderer setup field_model : ",field_model);
      if(field_type === "one2many" && field_name && field_model) {
        const result = await rpc("/get/limit", {
                    field_name,
                    field_model
                });
                // console.log("✅ RPC result:", result);
                this.xlimit = result;
      }
    })
    // console.log("getting all props : ", this.props);
  },

});

ListRenderer.rowsTemplate = "rp_one2many_limit.ListRenderer.Rows";
