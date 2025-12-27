from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


User = get_user_model()


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "position",
            "email",
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "A user with this email already exists."
            )

        return email

    # ✅ Extra safety: atomic save
    def save(self, commit=True):

        user = super().save(commit=False)
        user.email = user.email.lower()

        if commit:
            user.save()

        return user


class WorkerUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "position",
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")

        # ✅ Allow user to keep their own email
        qs = User.objects.filter(email=email)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError(
                "A user with this email already exists."
            )

        return email
