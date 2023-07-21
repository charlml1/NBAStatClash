from django import forms
from .models import Player

PLAYER_CHOICES = [tuple([p.name, p.name]) for p in Player.objects.all()]

class PlayerForm(forms.Form):
	player1 = forms.CharField(label="Player 1:", widget = forms.Select(choices=PLAYER_CHOICES))
	player2 = forms.CharField(label="Player 2:", widget = forms.Select(choices=PLAYER_CHOICES))

class PointsForm(forms.Form):
	fga = forms.FloatField(label ="Field Goals Attempted")
	fgm = forms.FloatField(label ="Field Goals Made")
	fta = forms.FloatField(label ="Free Throws Attempted")
	ftm = forms.FloatField(label ="Free Throws Made")
	threepm = forms.FloatField(label ="3 Pointers Made")
	pts = forms.FloatField(label ="Points")
	reb = forms.FloatField(label ="Rebounds")
	ast = forms.FloatField(label ="Assists")
	stl = forms.FloatField(label ="Steals")
	blk = forms.FloatField(label ="Blocked Shots")
	tov = forms.FloatField(label ="Turnovers")