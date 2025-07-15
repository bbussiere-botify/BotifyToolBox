import requests
import polling
import gzip
import shutil
import random
import time
import json
import urllib
from pprint import pprint



class BotifyAPI:
    def __init__(self, token, username, project_slug, debug=False):
        self.token = token
        self.username = username
        self.project_slug = project_slug
        self.debug = debug
        self.headers = {
            "Authorization": "Token {0}".format(self.token),
            "Content-type": "application/json"
        }

    def __get(self,url):
        try:
            r = requests.get(url, headers=self.headers)
        except requests.exceptions.RequestException as e:
            print(e)
            return False
        return r.json()

    def __post(self, url, data):
        try:
            r = requests.post(url, headers=self.headers, data=data)
        except requests.exceptions.RequestException as e:
            print(e)
            return False
        return r.json()

    def setDebug(self, newValue):
        self.debug = newValue

    def getLastAnalysis(self):
        urlGetLastProject = "https://api.botify.com/v1/analyses/{0}/{1}/light".format(self.username, self.project_slug)
        if self.debug:
            pprint("getLastProjects " + urlGetLastProject)
        results = self.__get(urlGetLastProject)
        if self.debug:
            pprint(results)

        return results

    def getLastAnalysisFull(self):
        urlGetLastProject = "https://api.botify.com/v1/analyses/{0}/{1}".format(self.username, self.project_slug)
        if self.debug:
            pprint("getLastProjects " + urlGetLastProject)
        results = self.__get(urlGetLastProject)
        if self.debug:
            pprint(results)

        return results

    def getTheLastAnalysis(self):
        allProjects = self.getLastAnalysis()
        if "results" in allProjects:
            for currentResult in allProjects["results"]:
                if "status" in currentResult and currentResult["status"] == "success":
                    return currentResult["slug"]
        return False

    def getAnalysisSummary(self, Analyse):
        urlgetAnalysisSummary = "https://api.botify.com/v1/analyses/{0}/{1}/{2}".format(self.username,
                                                                                        self.project_slug, Analyse)
        if self.debug:
            pprint("getAnalysisSummary " + urlgetAnalysisSummary)
        results = self.__get(urlgetAnalysisSummary)
        if self.debug:
            pprint(results)
        return results

    def getUrlDetail(self, Analyse, URL, Fields):
        urlgetUrlDetail = "https://api.botify.com/v1/analyses/{0}/{1}/{2}/urls/{3}?fields={4}".format(
            self.username,self.project_slug, Analyse, URL, Fields)
        if self.debug:
            pprint("getAnalysisSummary " + urlgetUrlDetail)
        results = self.__get(urlgetUrlDetail)
        if self.debug:
            pprint(results)
        return results

    def getUrlsAggs(self, Analyse, BQLRequest):
        getUrlsAggs = "https://api.botify.com/v1/analyses/{0}/{1}/{2}/urls/aggs".format(self.username,
                                                                                        self.project_slug, Analyse)
        if self.debug:
            pprint("getUrlsAggs " + getUrlsAggs)
        results = self.__post(getUrlsAggs, BQLRequest)
        if self.debug:
            pprint(results)
        return results

    def getQuery(self, BQLRequest):
        getUrlQuery = "https://api.botify.com/v1/projects/{0}/{1}/query".format(self.username,
                                                                                        self.project_slug)
        if self.debug:
            pprint("getQuery " + getUrlQuery)
        results = self.__post(getUrlQuery, BQLRequest)
        if self.debug:
            pprint(results)
        return results
    def getUrlsAggsBLA(self, startDate, endDate, BQLRequest):
        getUrlsAggsBLA = "https://app.botify.com/api/v1/logs/{0}/{1}/segments/{2}/{3}/aggs".format(self.username,
                                                                                        self.project_slug, startDate, endDate)
        if self.debug:
            pprint("getUrlsAggsBLA " + getUrlsAggsBLA)
        results = self.__post(getUrlsAggsBLA, BQLRequest)
        if self.debug:
            pprint(results)
        return results

    def getUrlsDetailsBLA(self, startDate, endDate, BQLRequest,page=1, size=50, sampling=100):
        getUrlsAggsBLA = "https://app.botify.com/api/v1/logs/{0}/{1}/urls/{2}/{3}?page={4}&size={5}&sampling={6}".format(
                                                self.username,self.project_slug,startDate, endDate,page,size,sampling)
        if self.debug:
            pprint("getUrlsDetailsBLA " + getUrlsAggsBLA)
        results = self.__post(getUrlsAggsBLA, BQLRequest)
        if self.debug:
            pprint(results)
        return results


    def getUrlDetails(self, Analyse, BQLRequest):
        urlList = "https://api.botify.com/v1/analyses/{0}/{1}/{2}/urls".format(self.username, self.project_slug,
                                                                               Analyse)
        if self.debug:
            pprint("getUrlDetails " + urlList)
        results = self.__post(urlList, BQLRequest)
        if self.debug:
            pprint(results)
        return results

    def getUrlHTML(self, Analyse, URL):
        urlList = "https://app.botify.com/api/v1/analyses/{0}/{1}/{2}/urls/html/{3}".format(self.username,
                                                                                            self.project_slug,
                                                                               Analyse, urllib.parse.quote(URL,safe=""))
        if self.debug:
            pprint("getUrlHTML " + urlList)
        results = self.__get(urlList)
        if self.debug:
            pprint(results)
        return results

    def getProjectCollections(self):
        allCollections = "https://api.botify.com/v1/projects/{0}/{1}/collections".format(self.username,
                                                                                        self.project_slug)
        if self.debug:
            pprint("getProjectCollections " + allCollections)
        results = self.__get(allCollections)
        if self.debug:
            pprint(results)
        return results

    def getCollectionDetail(self, collectionID):
        collection = "https://api.botify.com/v1/projects/{0}/{1}/collections/{2}".format(self.username,
                                                                                        self.project_slug, collectionID)
        if self.debug:
            pprint("getCollectionDetail " + collection)
        results = self.__get(collection)
        if self.debug:
            pprint(results)
        return results

    def projectQuery(self, BQLRequest, page=1, count=False):
        queryCollection = "https://api.botify.com/v1/projects/{0}/{1}/query?page={2}".format(self.username,
                                                                                          self.project_slug, page)
        if count:
            queryCollection+="&count"

        if self.debug:
            pprint("projectQuery " + queryCollection)
        results = self.__post(queryCollection, BQLRequest)
        if self.debug:
            pprint(results)
        return results

    def _checkJob(self, url):
        if self.debug:
            pprint("Check Status " + url)
        results = self.__get(url)
        if self.debug:
            pprint(results)

        if "job_status" in results and results["job_status"] == "DONE":
            if "download_url" in results["results"]:
                return results["results"]["download_url"]
            else:
                if self.debug:
                    pprint("Error No downloading url found ")
                    pprint(results)
                return True
        
        if "job_status" in results and results["job_status"] == "FAILED":
            if self.debug:
                pprint("Failed Job")
                pprint(results)
            raise Exception("Job failed: " + str(results))
        else:
            return False

    def launchJob(self, BQLRequest):
        jobUrl = "https://api.botify.com/v1/jobs"
        if self.debug:
            pprint("launchJob " + jobUrl)
        results = self.__post(jobUrl, BQLRequest)
        if self.debug:
            pprint(results)
        if results and "job_status" in results and results["job_status"] == "CREATED":
            jobID = results["job_id"]
            urlgetUrlsExportStatus = "{0}/{1}".format(jobUrl, jobID)
            if self.debug:
                pprint("JobUrl " + urlgetUrlsExportStatus)
            try:
                urlDownload = polling.poll(
                    lambda: self._checkJob(urlgetUrlsExportStatus),
                    step=30,
                    poll_forever=3600)
                if self.debug:
                    pprint("URL is " + str(urlDownload))
                return urlDownload
            except Exception as e:
                if self.debug:
                    pprint("Job failed during polling: " + str(e))
                return False
        else:
            return False

    def getCSVExport(self, Analyse, BQLRequest):
        createUrlsExport = "https://api.botify.com/v1/analyses/{0}/{1}/{2}/urls/export".format(self.username,
                                                                        self.project_slug, Analyse)
        if self.debug:
            pprint("getCSVExport " + createUrlsExport)
        results = self.__post(createUrlsExport,BQLRequest)
        if self.debug:
            pprint(results)
        if results["job_status"] == "CREATED":
            jobID = results["job_id"]
            # analyses/{username}/{project_slug}/{analysis_slug}/urls/export/{url_export_id}
            urlgetUrlsExportStatus = "{0}/{1}".format(createUrlsExport, jobID)
            if self.debug:
                pprint("getCSVExport " + urlgetUrlsExportStatus)
            urlDownload = polling.poll(
                lambda: self._checkJob(urlgetUrlsExportStatus),
                step=30,
                poll_forever=3600)
            if self.debug:
                pprint("URL is " + urlDownload)
            return urlDownload
        else:
            return False

    def downloadFile(self, url):
        local_filename = url.split('/')[-1]
        response = requests.get(url, stream=True)
        with open(local_filename, 'wb') as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)
        return local_filename

    def uncompress(self, fileGz, fileOut):
        with gzip.open(fileGz, 'r') as f_in, open(fileOut, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

class SpeedWorkersAPI:
    def __init__(self, deliveryToken, inventoryToken, websiteId, clusterId, debug=False):
        self.deliveryToken = deliveryToken
        self.inventoryToken = inventoryToken
        self.websiteId = websiteId
        self.clusterId = clusterId
        self.debug = debug
        self.inventoryHeaders = {
            "X-Sw-Website-Id": "{0}".format(self.websiteId),
            "X-Sw-Token": "{0}".format(self.inventoryToken),
            "Content-type": "application/json"
        }
        self.deliveryHeaders = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip",
            "Accept-Language": "en-US,en;q=0.8,en-US;q=0.6,en;q=0.4",
            "X-Sw-Options-Auth": "{0}".format(self.websiteId)
        }

    def __get(self, url, headers):
        try:
            r = requests.get(url, headers=headers)
        except requests.exceptions.RequestException as e:
            print(e)
            return False
        return r

    def __post(self, url, headers, data):
        try:
            r = requests.post(url, headers=headers, data=data)
        except requests.exceptions.RequestException as e:
            print(e)
            return False
        return r.json()

    def setDebug(self, newValue):
        self.debug = newValue

    def divide_chunks(self, l, n):
        # looping till length l
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def checkConnectionEcho(self, url, userAgent="botify-bot-sw-test"):
        headers=self.deliveryHeaders
        randomNumber=str(random.randrange(10000,99999))
        headers["X-Sw-Options"] = "echo-{0}".format(randomNumber)
        headers["User-Agent"] = userAgent
        if self.debug:
            pprint("headers sent")
            pprint(headers)
        response = self.__get(url, headers=headers)
        headersReceived = response.headers
        if self.debug:
            pprint('response headers')
            pprint(headersReceived)
        if 'x-sw-status' in headersReceived:
            print("SpeedWorkers Status:"+headersReceived["x-sw-status"])
            if 'x-sw-echo' in headersReceived:
                if headersReceived['x-sw-echo'] == randomNumber:
                    print("Echo Successful")
                    return True
                else:
                    print("Wrong Echo Number")
                    print("Echo sent:{0}".format(randomNumber))
                    print("Echo received:" + headersReceived['x-sw-echo'])
                    return False
            else:
                print("No echo found")
                return False
        return False

    def _checkConnection(self, url, headerOption, expectedResult, userAgent="botify-bot-sw-test"):
        headers=self.deliveryHeaders
        headers["X-Sw-Options"] = headerOption
        headers["User-Agent"] = userAgent
        randomNumber=42
        if self.debug:
            pprint("headers sent")
            pprint(headers)
        response = self.__get(url, headers=headers)
        headersReceived = response.headers
        if self.debug:
            pprint('response headers')
            pprint(headersReceived)
        if 'x-sw-status' in headersReceived:
            print("SpeedWorkers Status:"+headersReceived["x-sw-status"])
            if 'x-sw-echo' in headersReceived:
                if headersReceived['x-sw-echo'] == randomNumber:
                    print("Echo Successful")
                else:
                    print("Wrong Echo Number")
                    print("Echo sent:{0}".format(randomNumber))
                    print("Echo received:" + headersReceived['x-sw-echo'])
            else:
                print("No echo found")



    def speedWorkerInventory(self, urls, operations, refreshPriority, device):
        #targetUrl = "https://{0}.api.speedworkers.com/inventory".format(self.clusterId)
        targetUrl = "https://api.{0}.speedworkers.com/inventory".format(self.clusterId)
        ##Warning to check if the documentaion has evolved with "https://api.[CLUSTER-ID].speedworker.com/inventory" or not
        headers = self.inventoryHeaders
        ##use of json.dumps to replace " instead of '
        body = '''
        {
            "operations": %s,
            "refreshPriority": "%s",
            "device": "%s",
            "urls": %s
        }'''%(operations,refreshPriority,device,json.dumps(urls))
        if self.debug:
            print("Post URL: {0}".format(targetUrl))
            print("Headers sent : {0}".format(headers))
            print("Body sent : {0}".format(body))
        response = self.__post(targetUrl, headers, body)
        #response=False
        #"{'avail': 996,'message': 'Succeeded Inventory Operation','processed': 2,'received': 2}")
        if self.debug:
            print(response)
        return response

    def refreshPages(self, UrlPages, refreshPriority="low", device="na"):
        numberOfPages = len(UrlPages)
        maxUrlPerBatch = 999
        maxBatch = round(numberOfPages/maxUrlPerBatch)
        if self.debug:
            pprint('Number of URLs : {0}'.format(numberOfPages))
            pprint('Number of Batch : {0}'.format(maxBatch))

        myTodo = list(self.divide_chunks(UrlPages, maxUrlPerBatch))
        i=1
        for curList in myTodo:
            print("Batch {0} / {1}".format(i,maxBatch))
            jsonRes = self.speedWorkerInventory(curList,'["REFRESH"]', refreshPriority, device)
            if jsonRes:
                if "message" in jsonRes:
                    print(jsonRes["message"])
                else:
                    print('No Message')
            else:
                print("Error during Post")
            #pprint(curList)
            ## Wait 1 minute between each batch (cf : https://developers.botify.com/docs/inventory-management-api)
            time.sleep(60)
            i+=1