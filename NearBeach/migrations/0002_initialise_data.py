# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-26 08:32
from __future__ import unicode_literals

from django.db import migrations


def initialise_data(apps, schema_editor):
    """
    The initial setup of the database should populate certain fields with
    the correct data. Otherwise certain features of the database will
    not function correctly.
    """
    db_alias = schema_editor.connection.alias

    # List of amount types
    list_of_amount_type = apps.get_model("NearBeach", "list_of_amount_type")
    list_of_amount_type.objects.using(db_alias).bulk_create([
        list_of_amount_type(amount_type_description="Fixed",list_order=0),
        list_of_amount_type(amount_type_description="Per Contract",list_order=1),
        list_of_amount_type(amount_type_description="Per Year",list_order=2),
        list_of_amount_type(amount_type_description="Per Month",list_order=3),
        list_of_amount_type(amount_type_description="Per Fortnight",list_order=4),
        list_of_amount_type(amount_type_description="Per Day",list_order=5),
        list_of_amount_type(amount_type_description="Per Hour",list_order=6),
    ])


    # List of bug clients
    list_of_bug_client = apps.get_model("NearBeach","list_of_bug_client")
    list_of_bug_client.objects.using(db_alias).bulk_create([
        list_of_bug_client(
            bug_client_name="Bugzilla",
            bug_client_api_url="/rest/",
            api_open_bugs="?open_status=True",
            api_search_bugs="bug?quicksearch=",
            api_bug="/show_bug.cgi?id=",
        )
    ])

    list_of_currency=apps.get_model("NearBeach","list_of_currency")
    list_of_currency.objects.using(db_alias).bulk_create([
        list_of_currency(currency_description='Australian dollar', currency_short_description='AUD', list_order='1'),
        list_of_currency(currency_description='Brazilian real', currency_short_description='BRL', list_order='2'),
        list_of_currency(currency_description='Canadian dollar', currency_short_description='CAD', list_order='3'),
        list_of_currency(currency_description='Euro', currency_short_description='EUR', list_order='4'),
        list_of_currency(currency_description='Hong Kong dollar', currency_short_description='HKD', list_order='5'),
        list_of_currency(currency_description='Indian rupee', currency_short_description='INR', list_order='6'),
        list_of_currency(currency_description='Japanese yen', currency_short_description='JPY', list_order='7'),
        list_of_currency(currency_description='Mexican peso', currency_short_description='MXN', list_order='8'),
        list_of_currency(currency_description='New Zealand dollar', currency_short_description='NZD', list_order='9'),
        list_of_currency(currency_description='Norwegian krone', currency_short_description='NOK', list_order='10'),
        list_of_currency(currency_description='Pound sterling', currency_short_description='GBP', list_order='11'),
        list_of_currency(currency_description='Renminbi', currency_short_description='CNY', list_order='12'),
        list_of_currency(currency_description='Russian ruble', currency_short_description='RUB', list_order='13'),
        list_of_currency(currency_description='Singapore dollar', currency_short_description='SGD', list_order='14'),
        list_of_currency(currency_description='South African rand', currency_short_description='ZAR', list_order='15'),
        list_of_currency(currency_description='South Korean won', currency_short_description='KRW', list_order='16'),
        list_of_currency(currency_description='Swedish krona', currency_short_description='SEK', list_order='17'),
        list_of_currency(currency_description='Swiss franc', currency_short_description='CHF', list_order='18'),
        list_of_currency(currency_description='Turkish lira', currency_short_description='TRY', list_order='19'),
        list_of_currency(currency_description='United States dollar', currency_short_description='USD',list_order='20'),
    ])

    list_of_lead_source=apps.get_model("NearBeach","list_of_lead_source")
    list_of_lead_source.objects.using(db_alias).bulk_create([
        list_of_lead_source(lead_source_description='Campaign', list_order='1'),
        list_of_lead_source(lead_source_description='Cold Call', list_order='2'),
        list_of_lead_source(lead_source_description='Conference', list_order='3'),
        list_of_lead_source(lead_source_description='Direct Mail', list_order='4'),
        list_of_lead_source(lead_source_description='Email', list_order='5'),
        list_of_lead_source(lead_source_description='Employee', list_order='6'),
        list_of_lead_source(lead_source_description='Existing Customer', list_order='7'),
        list_of_lead_source(lead_source_description='Partner', list_order='8'),
        list_of_lead_source(lead_source_description='Public Relations', list_order='9'),
        list_of_lead_source(lead_source_description='Self Generated', list_order='10'),
        list_of_lead_source(lead_source_description='Trade Show', list_order='11'),
        list_of_lead_source(lead_source_description='Web Site', list_order='12'),
        list_of_lead_source(lead_source_description='Word of mouth', list_order='13'),
        list_of_lead_source(lead_source_description='Other', list_order='14'),
    ])

    # List of contact types
    list_of_contact_types = apps.get_model("NearBeach", "list_of_contact_type")
    list_of_contact_types.objects.using(db_alias).bulk_create([
        list_of_contact_types(contact_type="Notes"),
        list_of_contact_types(contact_type="Phone"),
        list_of_contact_types(contact_type="Email"),
        list_of_contact_types(contact_type="Appointment"),

    ])

    list_of_opportunity_stage = apps.get_model("NearBeach", "list_of_opportunity_stage")
    list_of_opportunity_stage.objects.using(db_alias).bulk_create([
        list_of_opportunity_stage(list_order="1",opportunity_stage_description="Prospecting",probability_success="10"),
        list_of_opportunity_stage(list_order="2", opportunity_stage_description="Qualification",probability_success="20"),
        list_of_opportunity_stage(list_order="3", opportunity_stage_description="Needs Analysis",probability_success="30"),
        list_of_opportunity_stage(list_order="4", opportunity_stage_description="Value Proposition",probability_success="40"),
        list_of_opportunity_stage(list_order="5", opportunity_stage_description="Identifying Decision Makers",probability_success="50"),
        list_of_opportunity_stage(list_order="6", opportunity_stage_description="Perception Analysis",probability_success="60"),
        list_of_opportunity_stage(list_order="7", opportunity_stage_description="Proposal/Price Quote",probability_success="70"),
        list_of_opportunity_stage(list_order="8", opportunity_stage_description="Negotiation/Review",probability_success="80"),
        list_of_opportunity_stage(list_order="9", opportunity_stage_description="Closed Won",probability_success="100",opportunity_closed=True),
        list_of_opportunity_stage(list_order="10", opportunity_stage_description="Closed Lost",probability_success="0",opportunity_closed=True),
    ])

    #List of requirement items status
    list_of_requirement_item_status = apps.get_model("NearBeach","list_of_requirement_item_status")
    list_of_requirement_item_status.objects.using(db_alias).bulk_create([
        list_of_requirement_item_status(requirement_item_status="Draft"),
        list_of_requirement_item_status(requirement_item_status="Review"),
        list_of_requirement_item_status(requirement_item_status="Developing/Working"),
        list_of_requirement_item_status(requirement_item_status="Testing"),
        list_of_requirement_item_status(requirement_item_status="User Acceptance Testing"),
        list_of_requirement_item_status(requirement_item_status="Rework"),
        list_of_requirement_item_status(requirement_item_status="Implemented"),
        list_of_requirement_item_status(requirement_item_status="Finish"),
        list_of_requirement_item_status(requirement_item_status="Not Tested"),
        list_of_requirement_item_status(requirement_item_status="Obsolete"),
    ])

    #List of requirement items type
    list_of_requirement_item_type = apps.get_model("NearBeach","list_of_requirement_item_type")
    list_of_requirement_item_type.objects.using(db_alias).bulk_create([
        list_of_requirement_item_type(requirement_item_type="Informational"),
        list_of_requirement_item_type(requirement_item_type="Feature"),
        list_of_requirement_item_type(requirement_item_type="User Case"),
        list_of_requirement_item_type(requirement_item_type="User Interface"),
        list_of_requirement_item_type(requirement_item_type="Non Functional"),
        list_of_requirement_item_type(requirement_item_type="Constraint"),
        list_of_requirement_item_type(requirement_item_type="System Function"),

    ])


    #List of requirement  status
    list_of_requirement_status = apps.get_model("NearBeach","list_of_requirement_status")
    list_of_requirement_status.objects.using(db_alias).bulk_create([
        list_of_requirement_status(requirement_status="Backlog"),
        list_of_requirement_status(requirement_status="Blocked"),
        list_of_requirement_status(requirement_status="In Progress"),
        list_of_requirement_status(requirement_status="Testing/Review"),
        list_of_requirement_status(requirement_status="Closed",requirement_status_is_closed=True),
    ])

    #List of requirement type
    list_of_requirement_type = apps.get_model("NearBeach","list_of_requirement_type")
    list_of_requirement_type.objects.using(db_alias).bulk_create([
        list_of_requirement_type(requirement_type="Non Specific"),
        list_of_requirement_type(requirement_type="Customer Requirements"),
        list_of_requirement_type(requirement_type="System Requirements"),
    ])



    # List of titles
    list_of_titles = apps.get_model("NearBeach", "list_of_title")
    list_of_titles.objects.using(db_alias).bulk_create([
        list_of_titles(title="Mr"),
        list_of_titles(title="Ms"),
        list_of_titles(title="Mrs"),
        list_of_titles(title="Mx"),
    ])


    list_of_quote_stages = apps.get_model("NearBeach", "list_of_quote_stage")
    db_alias = schema_editor.connection.alias
    list_of_quote_stages.objects.using(db_alias).bulk_create([
        #Quote Stage
        list_of_quote_stages(quote_stage="Quote Draft",is_invoice=False,sort_order=1),
        list_of_quote_stages(quote_stage="Quote Negotiation",is_invoice=False,sort_order=2),
        list_of_quote_stages(quote_stage="Quote Delivered",is_invoice=False,sort_order=3),
        list_of_quote_stages(quote_stage="Quote On Hold",is_invoice=False,sort_order=4),
        list_of_quote_stages(quote_stage="Quote Confirmed",is_invoice=False,sort_order=5),
        list_of_quote_stages(quote_stage="Quote Close Accepted",is_invoice=False,sort_order=6,quote_closed=True),
        list_of_quote_stages(quote_stage="Quote Close Rejected",is_invoice=False,sort_order=7,quote_closed=True),
        list_of_quote_stages(quote_stage="Quote Close Lost",is_invoice=False,sort_order=8,quote_closed=True),
        list_of_quote_stages(quote_stage="Quote Close Dead",is_invoice=False,sort_order=9,quote_closed=True),
        #Invoice Stage
        list_of_quote_stages(quote_stage="Invoice Draft",is_invoice=True,sort_order=10),
        list_of_quote_stages(quote_stage="Invoice Negotiation",is_invoice=True,sort_order=11),
        list_of_quote_stages(quote_stage="Invoice Delivered",is_invoice=True,sort_order=12),
        list_of_quote_stages(quote_stage="Invoice On Hold",is_invoice=True,sort_order=13),
        list_of_quote_stages(quote_stage="Invoice Confirmed",is_invoice=True,sort_order=14),
        list_of_quote_stages(quote_stage="Invoice Close Accepted",is_invoice=True,sort_order=15,quote_closed=True),
        list_of_quote_stages(quote_stage="Invoice Close Rejected",is_invoice=True,sort_order=16,quote_closed=True),
        list_of_quote_stages(quote_stage="Invoice Close Lost",is_invoice=True,sort_order=17,quote_closed=True),
        list_of_quote_stages(quote_stage="Invoice Close Dead",is_invoice=True,sort_order=18,quote_closed=True),
    ])

    nearbeach_option = apps.get_model("NearBeach","nearbeach_option")
    db_alias = schema_editor.connection.alias
    nearbeach_option.objects.using(db_alias).bulk_create([
        nearbeach_option(story_point_hour_min=4,story_point_hour_max=10),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initialise_data),
    ]
