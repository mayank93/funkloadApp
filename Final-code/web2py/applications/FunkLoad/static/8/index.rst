======================
FunkLoad_ bench report
======================


:date: 2013-11-21 15:09:59
:abstract: Stress Testing on user supplied link
           Bench result of ``Stress.test_stress``: 
           Access (nb_time)s times the main url

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents
.. |APDEXT| replace:: \ :sub:`1.5`

Bench configuration
-------------------

* Launched: 2013-11-21 15:09:59
* From: artoo
* Test: ``test_Stress.py Stress.test_stress``
* Target server: http://search.iiit.ac.in/courses/www/index.php
* Cycles of concurrent users: [5, 10]
* Cycle duration: 5s
* Sleeptime between request: from 0.0s to 0.5s
* Sleeptime between test case: 0.01s
* Startup delay between thread: 0.01s
* Apdex: |APDEXT|
* FunkLoad_ version: 1.16.1


Bench content
-------------

The test ``Stress.test_stress`` contains: 

* 5 page(s)
* 0 redirect(s)
* 2 link(s)
* 2 image(s)
* 0 XML RPC call(s)

The bench contains:

* 1 tests
* 46 pages
* 106 requests


Test stats
----------

The number of Successful **Tests** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ================== ================== ================== ================== ==================
                CUs               STPS              TOTAL            SUCCESS              ERROR
 ================== ================== ================== ================== ==================
                  5              0.200                  1                  1             0.00%
 ================== ================== ================== ================== ==================



Page stats
----------

The number of Successful **Pages** Per Second (SPPS) over Concurrent Users (CUs).
Note that an XML RPC call count like a page.

 .. image:: pages_spps.png
 .. image:: pages.png

 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                CUs             Apdex*             Rating               SPPS            maxSPPS              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                  5              1.000          Excellent              4.600              6.000                 23                 23             0.00%              0.514              0.787              1.212              0.591              0.716              1.171              1.187
                 10              0.921               Good              4.600             10.000                 23                 23             0.00%              0.812              1.602              2.578              0.890              1.318              2.254              2.276
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Request stats
-------------

The number of **Requests** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                CUs             Apdex*            Rating*                RPS             maxRPS              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                  5              1.000          Excellent              8.600             19.000                 43                 43             0.00%              0.013              0.421              1.061              0.026              0.516              0.921              1.002
                 10              0.921               Good             12.600             48.000                 63                 63             0.00%              0.025              0.585              2.414              0.038              0.108              1.915              1.980
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Slowest requests
----------------

The 5 slowest average response time during the best cycle with **5** CUs:

* In page 001, Apdex rating: Excellent, avg response time: 0.99s, get: ``/courses/www/index.php``
  `Get url`
* In page 002, Apdex rating: Excellent, avg response time: 0.78s, get: ``/courses/www/index.php``
  `Get url`
* In page 004, Apdex rating: Excellent, avg response time: 0.72s, get: ``/courses/www/index.php``
  `Get url`
* In page 005, Apdex rating: Excellent, avg response time: 0.63s, get: ``/courses/www/index.php``
  `Get url`
* In page 003, Apdex rating: Excellent, avg response time: 0.59s, get: ``/courses/www/index.php``
  `Get url`

Page detail stats
-----------------


PAGE 001: Get url
~~~~~~~~~~~~~~~~~

* Req: 001, get, url ``/courses/www/index.php``

     .. image:: request_001.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      5              1.000          Excellent                  5                  5             0.00%              0.921              0.988              1.061              0.921              1.002              1.061              1.061
                     10              0.500               POOR                 10                 10             0.00%              1.689              1.970              2.414              1.867              1.946              2.414              2.414
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|
* Req: 002, link, url ``/courses/www/themes/default/images/favicon.png``

     .. image:: request_001.002.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      5              1.000          Excellent                  5                  5             0.00%              0.021              0.039              0.056              0.021              0.032              0.056              0.056
                     10              1.000          Excellent                 10                 10             0.00%              0.025              0.088              0.137              0.042              0.108              0.137              0.137
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|
* Req: 003, link, url ``/courses/www/themes/modern/css/css_global.css?build=11018``

     .. image:: request_001.003.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      5              1.000          Excellent                  5                  5             0.00%              0.044              0.062              0.083              0.044              0.060              0.083              0.083
                     10              1.000          Excellent                 10                 10             0.00%              0.052              0.098              0.129              0.080              0.097              0.129              0.129
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|
* Req: 004, image, url ``/courses/www/themes/default/images/logo/siel-logo-transparent.png``

     .. image:: request_001.004.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      5              1.000          Excellent                  5                  5             0.00%              0.024              0.042              0.060              0.024              0.040              0.060              0.060
                     10              1.000          Excellent                 10                 10             0.00%              0.034              0.062              0.109              0.038              0.061              0.109              0.109
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|
* Req: 005, image, url ``/courses/www/themes/default/images/others/transparent.gif``

     .. image:: request_001.005.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      5              1.000          Excellent                  5                  5             0.00%              0.013              0.029              0.051              0.013              0.026              0.051              0.051
                     10              1.000          Excellent                 10                 10             0.00%              0.026              0.045              0.068              0.033              0.047              0.068              0.068
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|

PAGE 002: Get url
~~~~~~~~~~~~~~~~~

* Req: 001, get, url ``/courses/www/index.php``

     .. image:: request_002.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      5              1.000          Excellent                  5                  5             0.00%              0.708              0.776              0.896              0.708              0.771              0.896              0.896
                     10              1.000          Excellent                  8                  8             0.00%              0.812              0.968              1.175              0.812              0.907              1.175              1.175
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|

PAGE 003: Get url
~~~~~~~~~~~~~~~~~

* Req: 001, get, url ``/courses/www/index.php``

     .. image:: request_003.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      5              1.000          Excellent                  5                  5             0.00%              0.514              0.589              0.665              0.514              0.591              0.665              0.665
                     10              1.000          Excellent                  5                  5             0.00%              1.257              1.294              1.322              1.257              1.286              1.322              1.322
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|

PAGE 004: Get url
~~~~~~~~~~~~~~~~~

* Req: 001, get, url ``/courses/www/index.php``

     .. image:: request_004.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      5              1.000          Excellent                  5                  5             0.00%              0.623              0.716              0.823              0.623              0.716              0.823              0.823
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|

PAGE 005: Get url
~~~~~~~~~~~~~~~~~

* Req: 001, get, url ``/courses/www/index.php``

     .. image:: request_005.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      5              1.000          Excellent                  3                  3             0.00%              0.600              0.633              0.660              0.600              0.639              0.660              0.660
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|

Definitions
-----------

* CUs: Concurrent users or number of concurrent threads executing tests.
* Request: a single GET/POST/redirect/xmlrpc request.
* Page: a request with redirects and resource links (image, css, js) for an html page.
* STPS: Successful tests per second.
* SPPS: Successful pages per second.
* RPS: Requests per second, successful or not.
* maxSPPS: Maximum SPPS during the cycle.
* maxRPS: Maximum RPS during the cycle.
* MIN: Minimum response time for a page or request.
* AVG: Average response time for a page or request.
* MAX: Maximmum response time for a page or request.
* P10: 10th percentile, response time where 10 percent of pages or requests are delivered.
* MED: Median or 50th percentile, response time where half of pages or requests are delivered.
* P90: 90th percentile, response time where 90 percent of pages or requests are delivered.
* P95: 95th percentile, response time where 95 percent of pages or requests are delivered.
* Apdex T: Application Performance Index, 
  this is a numerical measure of user satisfaction, it is based
  on three zones of application responsiveness:

  - Satisfied: The user is fully productive. This represents the
    time value (T seconds) below which users are not impeded by
    application response time.

  - Tolerating: The user notices performance lagging within
    responses greater than T, but continues the process.

  - Frustrated: Performance with a response time greater than 4*T
    seconds is unacceptable, and users may abandon the process.

    By default T is set to 1.5s this means that response time between 0
    and 1.5s the user is fully productive, between 1.5 and 6s the
    responsivness is tolerating and above 6s the user is frustrated.

    The Apdex score converts many measurements into one number on a
    uniform scale of 0-to-1 (0 = no users satisfied, 1 = all users
    satisfied).

    Visit http://www.apdex.org/ for more information.
* Rating: To ease interpretation the Apdex
  score is also represented as a rating:

  - U for UNACCEPTABLE represented in gray for a score between 0 and 0.5 

  - P for POOR represented in red for a score between 0.5 and 0.7

  - F for FAIR represented in yellow for a score between 0.7 and 0.85

  - G for Good represented in green for a score between 0.85 and 0.94

  - E for Excellent represented in blue for a score between 0.94 and 1.

Report generated with FunkLoad_ 1.16.1, more information available on the `FunkLoad site <http://funkload.nuxeo.org/#benching>`_.