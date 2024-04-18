from django import forms


from bulls_cows.models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['player_name']
        labels = {'player_name': 'Current PLAYER'}
        widgets = {
            'player_name': forms.TextInput(attrs={
                'title': 'Type new name and press "Change name" to change',
                'maxlength': '50',
                'class': 'name'})}
        
   
    def __init__(self, *args, **kwargs):
        super(PlayerForm, self).__init__(*args, **kwargs)
        # self.fields['player_name'].widget.attrs['placeholder'] = self.instance        
                
        self.widgets = {
            'player_name': forms.TextInput(attrs={
                'title': 'Type new name and press "Change name" to change',
                # 'maxlength': '20',
                'class': 'name',
                'placeholder': self.instance})
        }

#TODO

        # self.validators = {
        #     'player_name': []
        # }
      
  