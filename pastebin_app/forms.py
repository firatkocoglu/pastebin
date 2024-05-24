from django import forms


class PlainTextForm(forms.Form):
    text = forms.CharField(label="Your Plain Text", max_length=1000, required=True)
    expiry = forms.IntegerField(
        label="Expires In", initial=1, required=False, min_value=1
    )

    def __init__(self, *args, **kwargs):
        super(PlainTextForm, self).__init__(*args, **kwargs)
        self.fields["text"].widget.attrs["placeholder"] = "Type your text here"
        self.fields["text"].widget.attrs["class"] = "text"
        self.fields["expiry"].widget.attrs["class"] = "expiry"
