define([
    'jquery',
    'jupyter-js-widgets'
], function ($, widgets) {

    'use strict';
    var _getId = (function () {

            var cnt = 0;
            return function () {

                cnt += 1;
                return 'fileupload_' + cnt;
            }
    })();

    //// Attempting to use the StyleModel
    // var InputButtonStyle = widgets.StyleModel.extend({
    //   defaults() {
    //     return _.extend(super.defaults(), {
    //       _model_name = 'ButtonStyleModel';
    //       _model_module = '@jupyter-widgets/controls';
    //       _model_module_version = JUPYTER_CONTROLS_VERSION;
    //     });
    //   });
    // });


    var FileUploadView = widgets.DOMWidgetView.extend({

        render: function render () {

            FileUploadView.__super__.render.apply(this, arguments);
            var id = _getId();
            var label = this.model.get('label');

            this.model.on('change:label', this._handleLabelChange, this);
            var $label = $('<label />')
            .text(label)

            .addClass('btn btn-default')
            .attr('for', id)
            .appendTo(this.$el);

            $('<input />')
            .attr('type', 'file')
            .attr('id', id)
            .css('display', 'none')
            .appendTo($label);
        },

        _handleLabelChange: function() {
            var label = this.model.get('label');
            this.$el.children("label").contents().first().replaceWith(label);
        },

        events: {
            'change': '_handleFileChange'
        },
        _handleFileChange: function _handleFileChange (ev) {

            var file = ev.target.files[0];
            var that = this;
            if (file) {
                var fileReader = new FileReader();
                fileReader.onload = function fileReaderOnload () {

                    that.model.set('data_base64', fileReader.result);
                    that.touch();
                };
                fileReader.readAsDataURL(file);
            }
            else {
                that.send({ event: 'Unable to open file.' });
            }
            that.model.set('file_name', file.name);
            that.touch();
            that.model.set('file_size', file.size);
            that.touch();
        }
    });

    return { FileUploadView: FileUploadView };
});
