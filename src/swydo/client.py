"""
Swydo API main client object.
"""

import logging
import os
from enum import Enum, unique, auto

from bravado.client import SwaggerClient
from bravado.exception import HTTPNotFound
from bravado.requests_client import RequestsClient
from typing import Dict, Optional
from typing import Iterator
from typing import Any
from bravado.client import CallableOperation

# ======================================================================================================================
# Public Members
# ======================================================================================================================

class Enumerations:
    """
    Enumerations used in the context of the Swydo API.
    """

    @unique
    class UserState(Enum):
        """
        State of a User.
        """

        revoked = auto()
        """User is Revoked."""

        pending = auto()
        """User is Pending."""

        active = auto()
        """User is Active."""

    @unique
    class ComparePeriod(Enum):
        """
        Period to compare, in a Report or ReportTemplate.
        """
        previous = auto()
        """Compare to Previous Period"""

        lastYear = auto()
        """Compare to Last Year"""

        previousMonth = auto()
        """Compare to Previous Month"""

class SwydoClient(object):
    """
    Main class that allows communications with the Swydo API.
    """

    # ==================================================================================================================
    # Public Interface
    # ==================================================================================================================

    def __init__(self, apiKey: str) -> None:
        self._apiKey = apiKey
        self._bravadoClient: Optional[SwaggerClient] = None
        self._prepareBravadoClient()

    # ==================================================================================================================
    # Teams
    # ==================================================================================================================

    def getTeams(self) -> Iterator:
        """
        Returns a list of teams.
        """

        # TODO: parameters cancelled, paymentPlan, createdAt*, cancelledAt*, lastActiveAt*

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict()

        for item in self._yieldAllItems(params=params, itemsGetter=client.teams.getTeams):
            yield item

    def getTeam(self, teamId: str) -> Dict[str, str]:
        """
        Returns all available information for a single team.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
        )

        return client.teams.getTeam(**params).result()

    # ==================================================================================================================
    # Users
    # ==================================================================================================================

    def getTeamUsers(self, teamId: str) -> Iterator[Dict[str, str]]:
        """
        Returns a list of users for a team.
        """

        client = self._getSwaggerClient()

        # TODO: Add support for status
        params: Dict[str, Any] = dict(
            teamId=teamId,
        )

        for item in self._yieldAllItems(params=params, itemsGetter=client.teams.getTeamUsers):
            yield item

    def getTeamUser(self, teamId: str, userId: str) -> Dict[str, str]:
        """
        Returns all available information for a single user.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            userId=userId,
        )

        return client.teams.getTeamUser(**params).result()

    # ==================================================================================================================
    # BrandTemplates
    # ==================================================================================================================

    def getTeamBrandTemplates(self, teamId: str) -> Iterator[Dict[str, str]]:
        """
        Returns a list of brand templates.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
        )

        for item in self._yieldAllItems(params=params, itemsGetter=client.teams.getTeamBrandTemplates):
            yield item

    def getTeamBrandTemplate(self, teamId: str, brandTemplateId: str) -> Dict[str, str]:
        """
        Returns all available information for a single brand template.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            brandTemplateId=brandTemplateId,
        )

        return client.teams.getTeamBrandTemplate(**params).result()
    
    # ==================================================================================================================
    # ReportTemplates
    # ==================================================================================================================

    def getTeamReportTemplates(self, teamId: str) -> Iterator[Dict[str, str]]:
        """
        Returns a list of report templates.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
        )

        for item in self._yieldAllItems(params=params, itemsGetter=client.teams.getTeamReportTemplates):
            yield item

    def getTeamReportTemplate(self, teamId: str, reportTemplateId: str) -> Dict[str, str]:
        """
        Add a user to a team.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            reportTemplateId=reportTemplateId,
        )

        return client.teams.getTeamReportTemplate(**params).result()
    
    # ==================================================================================================================
    # Connections
    # ==================================================================================================================

    def getTeamConnections(self, teamId: str, userId: str = None, providerId: str = None) -> Iterator[Dict[str, str]]:
        """
        Returns a list of connections.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
        )

        if userId:
            params['userId'] = userId
        if providerId:
            params['providerId'] = providerId

        for item in self._yieldAllItems(params=params, itemsGetter=client.teams.getTeamConnections):
            yield item

    def getTeamConnection(self, teamId: str, connectionId: str) -> Dict[str, str]:
        """
        Returns all available information for a single connections.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            connectionId=connectionId,
        )

        return client.teams.getTeamConnection(**params).result()

    # ==================================================================================================================
    # Clients
    # ==================================================================================================================

    def getTeamClients(self, teamId: str) -> Iterator[Dict[str, Any]]:
        """
        Returns a list of clients.
        """

        client = self._getSwaggerClient()

        # TODO: Add support for contributor, archived
        params: Dict[str, Any] = dict(
            teamId=teamId,
        )

        for item in self._yieldAllItems(params=params, itemsGetter=client.teams.getTeamClients):
            yield item

    def getTeamClient(self, teamId: str, clientId: str) -> Dict[str, Any]:
        """
        Returns all available information for a single client.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            clientId=clientId,
        )

        return client.teams.getTeamClient(**params).result()

    def createTeamClient(
            self,
            teamId: str,
            name: str,
            description: Optional[str]=None,
            email: Optional[str]=None
    ) -> Dict[str, Any]:
        """
        Create a client.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            clientCreate=dict(
                name=name,
            )
        )

        if description:
            params['clientCreate']['description'] = description
        if email:
            params['clientCreate']['email'] = email

        return client.teams.createTeamClient(**params).result()

    def updateTeamClient(
            self,
            teamId: str,
            clientId: str,
            name: Optional[str]=None,
            description: Optional[str]=None,
            email: Optional[str]=None
    ) -> Dict[str, Any]:
        """
        Update an existing client with new values.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            clientId=clientId,
            clientUpdate=dict(),
        )

        if name:
            params['clientUpdate']['name'] = name
        if description:
            params['clientUpdate']['description'] = description
        if email:
            params['clientUpdate']['email'] = email

        return client.teams.updateTeamClient(**params).result()

    def archiveTeamClient(self, teamId: str, clientId: str) -> None:
        """
        Archive a client, archived clients can't be used anymore unless you unarchive them.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            clientId=clientId,
        )

        client.teams.archiveTeamClient(**params).result()

    def unarchiveTeamClient(self, teamId: str, clientId: str) -> None:
        """
        Unarchive a client, so they can be used again.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            clientId=clientId,
        )

        client.teams.unarchiveTeamClient(**params).result()

    # ==================================================================================================================
    # DataSources
    # ==================================================================================================================

    def getClientDataSources(self, teamId: str, clientId: str) -> Dict[str, Any]:
        """
        Get client's data sources.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            clientId=clientId,
        )

        try:
            return client.teams.getClientDataSources(**params).result()
        except HTTPNotFound as hnfe:
            try:
                # HACK: We catch the 404 message from Swydo, and just return an object with empty DataSources - this
                # makes more sense
                if hnfe.response.json()['error'] == "DATASOURCE_NOT_FOUND":
                    return {
                        'id': clientId,
                        'dataSources': [],
                    }
            except Exception:
                pass
            raise

    # ==================================================================================================================
    # FacebookAds DataSource
    # ==================================================================================================================

    def setClientDataSourceFacebookAds(
            self,
            teamId: str,
            clientId: str,
            connectionId: str,
            dataSourceId: str,
            dataSourceName: str,
            dataSourceCurrencyCode: str = None,
    ) -> Dict[str, Any]:
        """
        Set client's Facebook ads data source.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            clientId=clientId,
            dataSourceCreate=dict(
                connectionId=connectionId,
                scope=dict(
                    id=dataSourceId,
                    name=dataSourceName,
                ),
            )
        )

        if dataSourceCurrencyCode:
            params['dataSourceCreate']['scope']['currencyCode'] = dataSourceCurrencyCode

        return client.teams.setClientDataSourceFacebookAds(**params).result()

    def removeClientDataSourceFacebookAds(self, teamId: str, clientId: str) -> None:
        """
        Remove client's Facebook ads data source.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            clientId=clientId,
        )

        try:
            client.teams.removeClientDataSourceFacebookAds(**params).result()
        except HTTPNotFound as hnfe:
            try:
                # HACK: We catch the 404 message from Swydo, and just accept this error - this
                # makes more sense
                if hnfe.response.json()['error'] == "DATASOURCE_NOT_FOUND":
                    return
            except Exception:
                pass
            raise

    # ==================================================================================================================
    # FacebookGraph DataSource
    # ==================================================================================================================

    def setClientDataSourceFacebookGraph(
            self, teamId: str, clientId: str, connectionId: str, dataSourceId: str, dataSourceName: str, dataSourcePageId: str
    ) -> Dict[str, Any]:
        """
        Set client's Facebook Graph data source.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            clientId=clientId,
            dataSourceCreate=dict(
                connectionId=connectionId,
                scope=dict(
                    id=dataSourceId,
                    name=dataSourceName,
                    pageId=dataSourcePageId,
                ),
            )
        )

        return client.teams.setClientDataSourceFacebookGraph(**params).result()

    def removeClientDataSourceFacebookGraph(self, teamId: str, clientId: str) -> None:
        """
        Remove client's Facebook Graph data source.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            clientId=clientId,
        )

        try:
            client.teams.removeClientDataSourceFacebookGraph(**params).result()
        except HTTPNotFound as hnfe:
            try:
                # HACK: We catch the 404 message from Swydo, and just accept this error - this
                # makes more sense
                if hnfe.response.json()['error'] == "DATASOURCE_NOT_FOUND":
                    return
            except Exception:
                pass
            raise

    # ==================================================================================================================
    # GoogleAdWords DataSource
    # ==================================================================================================================

    def setClientDataSourceGoogleAdWords(
            self, teamId: str, clientId: str, connectionId: str, dataSourceClientId: str, dataSourceName: str, dataSourceCurrencyCode: str = None
    ) -> Dict[str, Any]:
        """
        Set client's AdWords data source.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            clientId=clientId,
            dataSourceCreate=dict(
                connectionId=connectionId,
                scope=dict(
                    clientId=dataSourceClientId,
                    name=dataSourceName,
                ),
            )
        )

        if dataSourceCurrencyCode:
            params['dataSourceCreate']['scope']['currencyCode'] = dataSourceCurrencyCode

        return client.teams.setClientDataSourceGoogleAdWords(**params).result()

    def removeClientDataSourceGoogleAdWords(self, teamId: str, clientId: str) -> None:
        """
        Remove client's AdWords data source.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            clientId=clientId,
        )

        try:
            client.teams.removeClientDataSourceGoogleAdWords(**params).result()
        except HTTPNotFound as hnfe:
            try:
                # HACK: We catch the 404 message from Swydo, and just accept this error - this
                # makes more sense
                if hnfe.response.json()['error'] == "DATASOURCE_NOT_FOUND":
                    return
            except Exception:
                pass
            raise

    # ==================================================================================================================
    # GoogleAnalytics DataSource
    # ==================================================================================================================

    def setClientDataSourceGoogleAnalytics(
            self, teamId: str, clientId: str, connectionId: str, dataSourceAccountId: str, dataSourceName: str, dataSourceAccountName: str,
            dataSourceWebPropertyId: str, dataSourceProfileId: str,
            dataSourceCurrencyCode: str = None
    ) -> Dict[str, Any]:
        """
        Set client's Analytics data source.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            clientId=clientId,
            dataSourceCreate=dict(
                connectionId=connectionId,
                scope=dict(
                    name=dataSourceName,
                    accountId=dataSourceAccountId,
                    accountName=dataSourceAccountName,
                    webPropertyId=dataSourceWebPropertyId,
                    profileId=dataSourceProfileId,
                ),
            )
        )

        if dataSourceCurrencyCode:
            params['dataSourceCreate']['scope']['currencyCode'] = dataSourceCurrencyCode

        return client.teams.setClientDataSourceGoogleAnalytics(**params).result()

    def removeClientDataSourceGoogleAnalytics(self, teamId: str, clientId: str) -> None:
        """
        Remove client's Analytics data source.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            clientId=clientId,
        )

        try:
            client.teams.removeClientDataSourceGoogleAnalytics(**params).result()
        except HTTPNotFound as hnfe:
            try:
                # HACK: We catch the 404 message from Swydo, and just accept this error - this
                # makes more sense
                if hnfe.response.json()['error'] == "DATASOURCE_NOT_FOUND":
                    return
            except Exception:
                pass
            raise

    # ==================================================================================================================
    # Reports
    # ==================================================================================================================

    def getTeamReports(self, teamId: str) -> Iterator[Dict[str, str]]:
        """
        Returns a list of reports.
        """

        client = self._getSwaggerClient()

        # TODO: Add support for archived, clientId, authorId, brandTemplateId, reportTemplateId
        params: Dict[str, Any] = dict(
            teamId=teamId,
        )

        for item in self._yieldAllItems(params=params, itemsGetter=client.teams.getTeamReports):
            yield item

    def getTeamReport(self, teamId: str, reportId: str) -> Dict[str, str]:
        """
        Returns all available information for a single report.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            reportId=reportId,
        )

        return client.teams.getTeamReport(**params).result()

    def createTeamReport(
            self,
            teamId: str,
            name: str,
            clientId: str,
            brandTemplateId: str,
            reportTemplateId: str,
            comparePeriod: Enumerations.ComparePeriod,
            authorId: str = None
    ) -> Dict[str, str]:
        """
        Create a new report.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            reportCreate=dict(
                name=name,
                clientId=clientId,
                brandTemplateId=brandTemplateId,
                reportTemplateId=reportTemplateId,
                comparePeriod=comparePeriod.name,
            )
        )

        if authorId:
            params['reportCreate']['authorId'] = authorId

        return client.teams.createTeamReport(**params).result()

    def deleteTeamReport(self, teamId: str, reportId: str) -> None:
        """
        Delete a new report
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            reportId=reportId,
        )

        return client.teams.deleteTeamReport(**params).result()

    def updateTeamReport(
            self,
            teamId: str,
            reportId: str,
            name: str = None,
            clientId: str = None,
            brandTemplateId: str = None,
            reportTemplateId: str = None,
            comparePeriod: Enumerations.ComparePeriod = None,
            authorId: str = None
    ) -> Dict[str, str]:
        """
        Update an existing report.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            reportId=reportId,
            reportUpdate=dict()
        )

        if name:
            params['reportUpdate']['name'] = name
        if clientId:
            params['reportUpdate']['clientId'] = clientId
        if brandTemplateId:
            params['reportUpdate']['brandTemplateId'] = brandTemplateId
        if reportTemplateId:
            params['reportUpdate']['reportTemplateId'] = reportTemplateId
        if comparePeriod:
            params['reportUpdate']['comparePeriod'] = comparePeriod.name
        if authorId:
            params['reportUpdate']['authorId'] = authorId

        return client.teams.updateTeamReport(**params).result()

    def shareTeamReport(self, teamId: str, reportId: str) -> None:
        """
        Share a report.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            reportId=reportId,
        )

        client.teams.shareTeamReport(**params).result()

    def unshareTeamReport(self, teamId: str, reportId: str) -> None:
        """
        Unshare a report.
        """

        client = self._getSwaggerClient()

        params: Dict[str, Any] = dict(
            teamId=teamId,
            reportId=reportId,
        )

        client.teams.unshareTeamReport(**params).result()

    # ==================================================================================================================
    # Private Members
    # ==================================================================================================================

    def _yieldAllItems(self, params: Dict[str, Any], itemsGetter: CallableOperation) -> Iterator[Dict[str, Any]]:

        currentIndex = 0
        totalItems = 0
        firstRun = True

        while firstRun or totalItems > currentIndex:

            firstRun = False

            params['skip'] = currentIndex
            result = itemsGetter(**params).result()
            currentIndex = currentIndex + len(result.get('items', []))
            totalItems = result.get('total', 0)

            for item in result.get('items', []):
                yield item

    def _getSwaggerClient(self) -> SwaggerClient:
        if not self._bravadoClient:
            raise Exception("Swydo Swagger client was not instantiated.")

        return self._bravadoClient

    def _prepareBravadoClient(self) -> None:
        """
        Get a Bravado client to the microservice.
        :return: bravado client.
        """

        swaggerFileLocation = os.path.dirname(os.path.abspath(__file__)) + '/swydo_api.yml'

        httpClient = RequestsClient()
        httpClient.set_basic_auth(
            'api.swydo.com',
            'API', self._apiKey
        )

        swaggerValidation = bool(__debug__)

        if not self._bravadoClient:

            logging.info('Getting OpenAPI definition from %s', swaggerFileLocation)

            try:
                self._bravadoClient = \
                    SwaggerClient.from_url(
                        'file://%s' % swaggerFileLocation,
                        http_client=httpClient,
                        config={
                            # === bravado config ===

                            # Determines what is returned by the service call.
                            'also_return_response': False,

                            # === bravado-core config ====

                            # On the client side, validate incoming responses
                            # On the server side, validate outgoing responses
                            'validate_responses': swaggerValidation,

                            # On the client side, validate outgoing requests
                            # On the server side, validate incoming requests
                            'validate_requests': swaggerValidation,

                            # Use swagger_spec_validator to validate the swagger spec
                            'validate_swagger_spec': swaggerValidation,

                            # Use Python classes (models) instead of dicts for #/definitions/{models}
                            # On the client side, this applies to incoming responses.
                            # On the server side, this applies to incoming requests.
                            #
                            # NOTE: outgoing requests on the client side and outgoing responses on the
                            #       server side can use either models or dicts.
                            'use_models': False,

                            # List of user-defined formats of type
                            # :class:`bravado_core.formatter.SwaggerFormat`. These formats are in
                            # addition to the formats already supported by the OpenAPI 2.0
                            # Specification.
                            'formats': [],

                            # Fill with None all the missing properties during object unmarshal-ing
                            'include_missing_properties': False,
                        }
                    )
                logging.info('Got OpenAPI spec successfully.')
                # _client.swagger_spec.api_url = 'http://%s:%s/beep' % config.microservices.beepEndpoint
                # self._bravadoClient.swagger_spec.api_url = '' % config.microservices.beepURL
            except Exception:
                self._bravadoClient = None
                logging.exception('Cannot find OpenAPI spec.')
                raise

# ======================================================================================================================
# Private Members
# ======================================================================================================================
