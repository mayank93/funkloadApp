======================
FunkLoad_ bench report
======================


:date: 2013-11-21 14:54:25
:abstract: Stress Testing on user supplied link
           Bench result of ``Stress.test_stress``: 
           Access (nb_time)s times the main url

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents
.. |APDEXT| replace:: \ :sub:`1.5`

Bench configuration
-------------------

* Launched: 2013-11-21 14:54:25
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

* 3 tests
* 44 pages
* 84 requests


Test stats
----------

The number of Successful **Tests** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ================== ================== ================== ================== ==================
                CUs               STPS              TOTAL            SUCCESS              ERROR
 ================== ================== ================== ================== ==================
                  5              0.400                  2                  2             0.00%
                 10              0.200                  1                  1             0.00%
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
                  5              0.988          Excellent              4.600              5.000                 23                 23             0.00%              0.236              0.762              1.980              0.425              0.751              1.277              1.402
                 10              1.000          Excellent              4.200              5.000                 21                 21             0.00%              0.356              0.749              1.386              0.472              0.603              1.298              1.323
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
                  5              0.988          Excellent              8.600             19.000                 43                 43             0.00%              0.018              0.408              1.849              0.023              0.240              0.873              1.156
                 10              1.000          Excellent              8.200             20.000                 41                 41             0.00%              0.016              0.384              1.259              0.025              0.356              0.951              1.086
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Slowest requests
----------------

The 5 slowest average response time during the best cycle with **5** CUs:

* In page 001, Apdex rating: Good, avg response time: 1.01s, get: ``/courses/www/index.php``
  `Get url`
* In page 004, Apdex rating: Excellent, avg response time: 0.75s, get: ``/courses/www/index.php``
  `Get url`
* In page 002, Apdex rating: Excellent, avg response time: 0.65s, get: ``/courses/www/index.php``
  `Get url`
* In page 003, Apdex rating: Excellent, avg response time: 0.63s, get: ``/courses/www/index.php``
  `Get url`
* In page 005, Apdex rating: Excellent, avg response time: 0.56s, get: ``/courses/www/index.php``
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
                      5              0.900               Good                  5                  5             0.00%              0.634              1.013              1.849              0.634              0.758              1.849              1.849
                     10              1.000          Excellent                  5                  5             0.00%              0.951              1.097              1.259              0.951              1.086              1.259              1.259
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|
* Req: 002, link, url ``/courses/www/themes/default/images/favicon.png``

     .. image:: request_001.002.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      5              1.000          Excellent                  5                  5             0.00%              0.024              0.027              0.032              0.024              0.027              0.032              0.032
                     10              1.000          Excellent                  5                  5             0.00%              0.029              0.087              0.154              0.029              0.076              0.154              0.154
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|
* Req: 003, link, url ``/courses/www/themes/modern/css/css_global.css?build=11018``

     .. image:: request_001.003.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      5              1.000          Excellent                  5                  5             0.00%              0.041              0.049              0.056              0.041              0.050              0.056              0.056
                     10              1.000          Excellent                  5                  5             0.00%              0.057              0.067              0.078              0.057              0.069              0.078              0.078
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|
* Req: 004, image, url ``/courses/www/themes/default/images/logo/siel-logo-transparent.png``

     .. image:: request_001.004.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      5              1.000          Excellent                  5                  5             0.00%              0.019              0.032              0.039              0.019              0.033              0.039              0.039
                     10              1.000          Excellent                  5                  5             0.00%              0.023              0.027              0.035              0.023              0.025              0.035              0.035
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|
* Req: 005, image, url ``/courses/www/themes/default/images/others/transparent.gif``

     .. image:: request_001.005.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      5              1.000          Excellent                  5                  5             0.00%              0.018              0.020              0.023              0.018              0.019              0.023              0.023
                     10              1.000          Excellent                  5                  5             0.00%              0.016              0.029              0.045              0.016              0.027              0.045              0.045
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|

PAGE 002: Get url
~~~~~~~~~~~~~~~~~

* Req: 001, get, url ``/courses/www/index.php``

     .. image:: request_002.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      5              1.000          Excellent                  5                  5             0.00%              0.236              0.654              1.402              0.236              0.546              1.402              1.402
                     10              1.000          Excellent                  5                  5             0.00%              0.356              0.632              0.765              0.356              0.681              0.765              0.765
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|

PAGE 003: Get url
~~~~~~~~~~~~~~~~~

* Req: 001, get, url ``/courses/www/index.php``

     .. image:: request_003.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      5              1.000          Excellent                  5                  5             0.00%              0.425              0.629              0.926              0.425              0.601              0.926              0.926
                     10              1.000          Excellent                  4                  4             0.00%              0.508              0.557              0.611              0.508              0.578              0.611              0.611
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|

PAGE 004: Get url
~~~~~~~~~~~~~~~~~

* Req: 001, get, url ``/courses/www/index.php``

     .. image:: request_004.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      5              1.000          Excellent                  5                  5             0.00%              0.518              0.746              0.873              0.518              0.775              0.873              0.873
                     10              1.000          Excellent                  4                  4             0.00%              0.455              0.544              0.636              0.455              0.570              0.636              0.636
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|

PAGE 005: Get url
~~~~~~~~~~~~~~~~~

* Req: 001, get, url ``/courses/www/index.php``

     .. image:: request_005.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      5              1.000          Excellent                  3                  3             0.00%              0.490              0.558              0.656              0.490              0.528              0.656              0.656
                     10              1.000          Excellent                  3                  3             0.00%              0.472              0.542              0.597              0.472              0.557              0.597              0.597
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