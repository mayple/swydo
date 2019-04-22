# swydo

[![PyPI version](https://badge.fury.io/py/swydo.svg)](https://badge.fury.io/py/swydo)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/swydo.svg)](https://pypi.python.org/pypi/swydo/)
[![Build Status](https://travis-ci.com/mayple/swydo.svg?branch=master)](https://travis-ci.com/mayple/swydo)

> A Python 3 module to interact with the Swydo API.

Developed in [Mayple](https://www.mayple.com).

## Install

```sh
pip install swydo
```

## Example

```python
import logging
import swydo
import itertools
from bravado.exception import HTTPError

logging.basicConfig()

from typing import Dict, Union, Any

YOUR_API_KEY="..."

# Manually injected, as Swydo sometimes doesn't return teams
yourTeamId = "..."

print("Starting...")
swydoClient = swydo.SwydoClient(apiKey=YOUR_API_KEY)

yourBrandTemplateId = "..."
yourReportTemplateId = "..."
yourFacebookAdsConnectionId = "..."
yourFacebookGraphConnectionId = "..."
yourGoogleAdWordsConnectionId = "..."
yourGoogleAnalyticsConnectionId = "..."

# If you have one
testClientId = ""

skipInitialEnumeration = False

if not skipInitialEnumeration:
    teams = list(swydoClient.getTeams())

    for teamId in itertools.chain(
            (team['id'] for team in teams),
            [yourTeamId]
    ):
        team = swydoClient.getTeam(teamId)
        assert team['id'] == teamId
        print("Team: %s" % team)

        teamUsers = swydoClient.getTeamUsers(teamId=teamId)
        for userId in (user['id'] for user in teamUsers):
            user = swydoClient.getTeamUser(teamId=teamId, userId=userId)
            assert userId == user['id']
            print("User: %s" % user)

        teamConnections = swydoClient.getTeamConnections(teamId=teamId)
        for connectionId in (connection['id'] for connection in teamConnections):
            connection = swydoClient.getTeamConnection(teamId=teamId, connectionId=connectionId)
            assert connectionId == connection['id']
            print("Connection: %s" % connection)

        teamBrandTemplates = swydoClient.getTeamBrandTemplates(teamId=teamId)
        for brandTemplateId in (brandTemplate['id'] for brandTemplate in teamBrandTemplates):
            brandTemplate = swydoClient.getTeamBrandTemplate(teamId=teamId, brandTemplateId=brandTemplateId)
            assert brandTemplateId == brandTemplate['id']
            print("BrandTemplate: %s" % brandTemplate)

        teamReportTemplates = swydoClient.getTeamReportTemplates(teamId=teamId)
        for reportTemplateId in (reportTemplate['id'] for reportTemplate in teamReportTemplates):
            reportTemplate = swydoClient.getTeamReportTemplate(teamId=teamId, reportTemplateId=reportTemplateId)
            assert reportTemplateId == reportTemplate['id']
            print("ReportTemplate: %s" % reportTemplate)

        teamClients = swydoClient.getTeamClients(teamId=teamId)
        for clientId in (client['id'] for client in teamClients):
            client = swydoClient.getTeamClient(teamId=teamId, clientId=clientId)
            assert clientId == client['id']
            print("Client: %s" % client)

            clientDataSources = swydoClient.getClientDataSources(teamId=teamId, clientId=clientId)
            assert clientId == clientDataSources['id']
            print("ClientDataSources: %s" % clientDataSources)
            
        teamReports = swydoClient.getTeamReports(teamId=teamId)
        for reportId in (report['id'] for report in teamReports):
            report = swydoClient.getTeamReport(teamId=teamId, reportId=reportId)
            assert reportId == report['id']
            print("Report: %s" % report)

# Find a specific client
try:
    testClient: Union[None, Dict[str, Any]] = \
        swydoClient.getTeamClient(teamId=yourTeamId, clientId=testClientId)
except HTTPError as he:
    if he.status_code == 404:
        testClient = None
    else:
        raise
if not testClient:
    testClient = swydoClient.createTeamClient(
        teamId=yourTeamId,
        name="Test Client via API",
        description="Test Client's Description",
        email="test@email.com"
    )
print("Test Client: %s" % testClient)

testClient = swydoClient.updateTeamClient(
    teamId=yourTeamId,
    clientId=testClient['id'],
    name="Updated Test Client via API",
    description="Updated Test Client's Description",
)
print("Test Client: %s" % testClient)

swydoClient.archiveTeamClient(
    teamId=yourTeamId,
    clientId=testClient['id'],
)
print("Test Client archived.")

swydoClient.unarchiveTeamClient(
    teamId=yourTeamId,
    clientId=testClient['id'],
)
print("Test Client unarchived.")

swydoClient.removeClientDataSourceFacebookAds(
    teamId=yourTeamId,
    clientId=testClientId,
)
print("facebookAdsDataSource removed")

swydoClient.removeClientDataSourceFacebookGraph(
    teamId=yourTeamId,
    clientId=testClientId,
)
print("FacebookGraph DataSource removed")

swydoClient.removeClientDataSourceGoogleAdWords(
    teamId=yourTeamId,
    clientId=testClientId,
)
print("GoogleAdWords DataSource removed")

swydoClient.removeClientDataSourceGoogleAnalytics(
    teamId=yourTeamId,
    clientId=testClientId,
)
print("GoogleAnalytics DataSource removed")

# FacebookAds
facebookAdsDataSource = swydoClient.setClientDataSourceFacebookAds(
    teamId=yourTeamId,
    clientId=testClientId,
    connectionId=yourFacebookAdsConnectionId,
    dataSourceId='adAccountId',
    dataSourceName='Added Facebook Ad Account',
    dataSourceCurrencyCode='USD',
)
print("FacebookAds DataSource: %s" % facebookAdsDataSource)

# FacebookGraph
facebookGraphDataSource = swydoClient.setClientDataSourceFacebookGraph(
    teamId=yourTeamId,
    clientId=testClientId,
    connectionId=yourFacebookGraphConnectionId,
    dataSourceId='dataSourceId',
    dataSourceName='Added Facebook Graph Account',
    dataSourcePageId='dataSourcePageId',
)
print("FacebookGraph DataSource: %s" % facebookGraphDataSource)

# GoogleAdWords
googleAdWordsDataSource = swydoClient.setClientDataSourceGoogleAdWords(
    teamId=yourTeamId,
    clientId=testClientId,
    connectionId=yourGoogleAdWordsConnectionId,
    dataSourceClientId='dataSourceClientId',
    dataSourceName='Added Google Ads Account',
    dataSourceCurrencyCode='USD',
)
print("GoogleAdWords DataSource: %s" % googleAdWordsDataSource)

# GoogleAnalytics
googleAnalyticsDataSource = swydoClient.setClientDataSourceGoogleAnalytics(
    teamId=yourTeamId,
    clientId=testClientId,
    connectionId=yourGoogleAnalyticsConnectionId,
    dataSourceAccountId='dataSourceAccountId',
    dataSourceName='Added Google Analytics Account',
    dataSourceAccountName='dataSourceAccountName',
    dataSourceWebPropertyId='dataSourceWebPropertyId',
    dataSourceProfileId='dataSourceProfileId',
    dataSourceCurrencyCode='USD',
)
print("GoogleAnalytics DataSource: %s" % googleAnalyticsDataSource)

# Create a report
testReport = swydoClient.createTeamReport(
    teamId=yourTeamId,
    name="Temporary Report",
    clientId=testClientId,
    brandTemplateId=yourBrandTemplateId,
    reportTemplateId=yourReportTemplateId,
    comparePeriod=swydo.Enumerations.ComparePeriod.previous,
)
print("TestReport: %s" % testReport)
testReportId = testReport['id']

# Share the report
swydoClient.shareTeamReport(
    teamId=yourTeamId,
    reportId=testReportId,
)

# Update the report
testReport = swydoClient.updateTeamReport(
    teamId=yourTeamId,
    reportId=testReportId,
    name="Temporary Report Updated",
)
print("TestReport: %s" % testReport)
testReportId = testReport['id']

# Unshare the report
swydoClient.unshareTeamReport(
    teamId=yourTeamId,
    reportId=testReportId,
)

# Delete the report
swydoClient.deleteTeamReport(
    teamId=yourTeamId,
    reportId=testReportId,
)

swydoClient.removeClientDataSourceFacebookAds(
    teamId=yourTeamId,
    clientId=testClientId,
)
print("facebookAdsDataSource removed")

swydoClient.removeClientDataSourceFacebookGraph(
    teamId=yourTeamId,
    clientId=testClientId,
)
print("FacebookGraph DataSource removed")

swydoClient.removeClientDataSourceGoogleAdWords(
    teamId=yourTeamId,
    clientId=testClientId,
)
print("GoogleAdWords DataSource removed")

swydoClient.removeClientDataSourceGoogleAnalytics(
    teamId=yourTeamId,
    clientId=testClientId,
)
print("GoogleAnalytics DataSource removed")

print("Success!...")
```

## Contributing

Pull requests and stars are always welcome. For bugs and feature requests, [please create an issue](https://github.com/mayple/swydo/issues/new).

Install with:
```sh
$ virtualenv .venv -p python3
$ . .venv/bin/activate
(.venv) $ pip install -r requirements.txt
```
and run the tests with:
```sh
(.venv) $ pip install -r tests/requirements.txt
(.venv) $ pytest tests/
```
documentation can be generated like this:
```sh
(.venv) $ pip install -r doc/requirements.txt
(.venv) $ sphinx-build -b html doc doc/_build/html
```

## Related Projects

Used [cookiecutter Python library template](https://github.com/mdklatt/cookiecutter-python-lib) by [mdklatt](https://github.com/mdklatt).

## Author

**Alon Diamant (advance512)**

* [github/advance512](https://github.com/advance512)
* [Homepage](http://www.alondiamant.com)
