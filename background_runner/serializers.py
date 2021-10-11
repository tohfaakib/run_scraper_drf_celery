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

category_choices = (
    ('title_filmmakers_music_department_sortable_table', 'Music Department'),
    ('title_filmmakers_director_sortable_table', 'Directors'),
    ('title_filmmakers_writer_sortable_table', 'Writers'),
    ('title_filmmakers_producer_sortable_table', 'Producers'),
    ('title_filmmakers_production_designer_sortable_table', 'Production Designers'),
    ('title_filmmakers_production_manager_sortable_table', 'Production Manager'),
    ('title_filmmakers_art_department_sortable_table', 'Art Department'),
    ('title_filmmakers_sound_department_sortable_table', 'Sound Department'),
    ('title_filmmakers_visual_effects_sortable_table', 'Visual Effects'),
    ('title_filmmakers_animation_department_sortable_table', 'Animation Department'),
    ('title_filmmakers_casting_department_sortable_table', 'Casting Department'),
    ('title_filmmakers_editorial_department_sortable_table', 'Editorial Department'),
    ('title_filmmakers_script_department_sortable_table', 'Script Department'),
    ('title_filmmakers_miscellaneous_sortable_table', 'Additional Crew'),
    ('title_filmmakers_thanks_sortable_table', 'Thanks'),
)


class TriggerSerializer(serializers.Serializer):
    """Your data serializer, define your fields here."""
    # start_url = serializers.CharField(max_length=250, required=False)
    start_url = serializers.ChoiceField(choices=CHOICES)
    start_page_number = serializers.CharField(max_length=250, required=False)
    category_id = serializers.ChoiceField(choices=category_choices)
