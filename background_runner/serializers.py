from rest_framework import serializers

CHOICES = (
    ('https://pro.imdb.com/discover/title?type=any&sortOrder=MOVIEMETER_ASC&ref_=nv_tt_tmm', 'Top MOVIEmeter'),
    ('https://pro.imdb.com/discover/title?type=movie&status=development&sortOrder=MOVIEMETER_ASC&ref_=nv_tt_dev',
     'Movies in Development'),
    ('https://pro.imdb.com/discover/title?type=movie&status=pre_production&sortOrder=MOVIEMETER_ASC&ref_=nv_tt_pre',
     'Movies in Pre-Production'),
    ('https://pro.imdb.com/discover/title?type=movie&status=production&sortOrder=MOVIEMETER_ASC&ref_=nv_tt_prod',
     'Movies in Production'),
    ('https://pro.imdb.com/discover/title?type=movie&status=post_production&sortOrder=MOVIEMETER_ASC&ref_=nv_tt_post',
     'Movies in Post-Production'),
    ('https://pro.imdb.com/discover/title?type=movie&status=released&sortOrder=MOVIEMETER_ASC&ref_=nv_tt_rel',
     'Released Movies'),
    (
    'https://pro.imdb.com/discover/title?type=tvSeries%2CtvEpisode%2CtvMovie%2CtvMiniSeries%2CtvSpecial%2CtvShort&status=production&sortOrder=MOVIEMETER_ASC&ref_=nv_tt_tv_prod',
    'TV in Production'),
)


class TriggerSerializer(serializers.Serializer):
    """Your data serializer, define your fields here."""
    # start_url = serializers.CharField(max_length=250, required=False)
    start_url = serializers.ChoiceField(choices=CHOICES)

    start_page_number = serializers.CharField(max_length=250, required=False)
