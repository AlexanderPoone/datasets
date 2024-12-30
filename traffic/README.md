# FossTraffic Framework

Re-adapted from 22' Project. ([full paper here](#))

### `Main.vue`

We are a small but dedicated team based in Barnet, London, providing battle-proven real-time Intelligent Video Analytics (IVA) services. Our services run on NVIDIA® GeForce® RTX 4000 Series GPUs.

Reasons to Choose FossTraffic's Services over Outsourcing to Places like China and India:

* Speed: Rust technology is not interpreted line by line but compiled, ensuring **high server performance**. We use Apache Parquet (`fastparquet`) to store all analytics: `conda install fastparquet`, which enables **fast data operations and compression**.
* Scalability: Our Nginx-based **load balancing** technology guarantees scalable solutions.
* Safety of Data: Our services are **ISO27001-audited**. We also use containerisation technology for **full isolation**, mitigating risks to data security
* Secure Payment: We use the trusted Braintree payment services which supports multiple online methods.
* Soundness: All machine learning results are **interpretable** by scientific statistical concepts, which we will turn into simple language.
* Support the Open Source Community: We embrace open source software unlike large firms, that's why our name's FossTraffic.

(`oblique` tracking model: Also test vehicle number plate recognition for tracking/blurring and face recognition for blurring. [Supports United Kingdom, Hong Kong, Macau and Chinese vehicle number plates at the moment. Note that for Hong Kong registration plates, the letters 'I' and 'O' are disallowed, they are merged into '1' and '0'.])

Future domain: `enquiries@fosstraffic.com`

## Project Structure
* Front end
  * `Main.vue`
  * `Mgmt.vue`
  * `Upload.vue`
  * `UserSettings.vue`
  * `Billing.vue` (receipts)
  * `/register`
  * `/register2`
  * `/register3`
  * `/activate?token=`
  * `PrivacyPolicy.vue`
* Mobile end
  * `main.dart` (just `webview_flutter` to save time + `adsense`)
* Back end
  * `backend.py`

## `Mgmt.vue` Online Training Set Management System, OTSMS

Vue 3, Vuetify 3

Dataset name is a `<v-select></v-select>` (content: 2. Cloudy morning, 3. Bright morning, 4. Rainy morning…).

`<v-text-field></v-text-field>` for name (id autofill in).

`<v-data-table></v-data-table>` for displaying all data subsets.

## `Upload.vue` Upload portal

```html
<p><v-btn><i class="fa-duotone fa-fw fa-upload"></i> Upload footage (length up to 10 hours)</v-btn>,</p>

<p>or enter .m3u8 / YouTube URL: <v-text-field></v-text-field></p>

<v-dialog
  v-model="dialog"
  width="auto"
>
  <v-card
    max-width="400"
    prepend-icon="mdi-update"
    title="Error"
    text="The entered footage format is not supported. We support .m3u8 / YouTube URLs."
  >
    <template v-slot:actions>
      <v-btn
        class="ms-auto"
        text="Ok"
        @click="dialog = false"
      ></v-btn>
    </template>
  </v-card>
</v-dialog>
```

```mongo
use fosstraffic
db.createCollection("users")
db.createCollection("sessions")
db.createCollection("cctvs")
db.createCollection("roadsegments")
db.createCollection("history")
db.createCollection("weather")
db.createCollection("trainingsamples")
```

TODO: 

1. Deploy `scheduledTask.py` to my computer. `wfastcgi`
2. Set up MongoDB and Docker.
3. Task scheduler put predictions in the `predictions` collection of MongoDB. (Luxi Sans)
4. Interpretation (XAI): Show wordcloud and SHAP chart.
5. CSS should be common at `static/styles.css`.

## Cronjobs
1. Speed should become real-time.
2. Get weather in 'mailing list' (collection 'weatherzone', 'username_list')

## Branding
Celadon on Black, Luxi Sans font

## Monetisation
### `UserSettings.vue` Braintree
The sandbox offers you a space to test payment processing without risking your actual credit card details. Braintree: <https://github.com/braintree/braintree_express_example/issues/28>

### `Billing.vue`
`<v-data-table></v-data-table>` of transactions, each row contains `<v-btn>Download receipt</v-btn>` generated from `receipt.jinja2` by WeasyPrint.

### AdSense
Left, right & bottom Banner Ads
https://www.google.com/adsense/new/u/0/pub-9627209153774793/home
https://support.google.com/adsense/answer/9274516?hl=en

## Outer structure
### Landing page
* Remove Facebook and Dribble from Vue template
* Needs a translation script to turn Excel spreadsheet into `vue-i18n` format.

#### Landing page sections

```jinja
<template>
  <v-parallax
    dark
    src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg"
  >
    <v-row
      align="center"
      justify="center"
    >
      <v-col
        class="text-center"
        cols="12"
      >
        <h1 class="text-h4 font-weight-thin mb-4">
          FossTraffic
        </h1>
        <h4 class="subheading">
          Free registration!
        </h4>
      </v-col>
    </v-row>
  </v-parallax>
</template>

<section>
	<div class="leftblock">
	<h1>Much affordable than Amazon and Google</h1>
	<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
	</div>

	<div class="rightblock">
	<h1>24-hour Fast Support which Amazon and Google will Never Provide</h1>
	<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
	</div>

	<div class="leftblock">
	<h1>Pretrained Battle-proven Models</h1>
	<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
	</div>

	<div class="rightblock">
	<h1>Live Demonstration & Testimonials</h1>
	<p>Test stream goes here <video></video></p>
	</div>

	<div class="leftblock">
	<h1>Iron-clad Security with Role-based Access Control</h1>
	<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
	</div>
</section>
```

### 3D Conversion and Info Extraction
* `engine_3d.py` is still here

Template location: `/templates/3dconv.jinja2`
```jinja
    <h1 class="fosstraffic-header">3D Conversion and Info Extraction</h1>
    <h2>Try here!</h2>
    <div class="mb-3 row">
        <label for="input3dFile" class="col-sm-2 col-form-label">Input 3D Model File</label>
        <div class="col-sm-10">
        <input class="form-control" type="file" id="input3dFile" accept=".zip, .tar, .tar.gz, .7z, .glb">
        </div>
    </div>
    {% if progressPerc < 100 %}
    <div class="progress">
      <div class="progress-bar" role="progressbar" style="width: {{progressPerc}}%;" aria-valuenow="{{progressPerc}}" aria-valuemin="0" aria-valuemax="100">{{progressPerc}}%</div>
    </div>
    {% else %}
    <div class="mb-3 row">
        <div class="col-sm-6">THREE.JS Preview goes here</div>
        <div class="col-sm-6" style="background: silver;">
            <p><strong>Primitive type</strong>: {{meshinfo.primitiveType}}</p><!--Triangles-->
            <p><strong>Number of primitives</strong>: {{meshinfo.numPrimitives}}</p><!--418,000-->
            <p><strong>Bounding box dimensions</strong>: ({{meshinfo.boundingBoxX}} px, {{meshinfo.boundingBoxY}} px, {{meshinfo.boundingBoxZ}} px)</p><!--(13.75 px, 11.07 px, 8.83 px)-->
            <p><strong>Centre of mass</strong>: ({{meshinfo.centreOfMassX}}, {{meshinfo.centreOfMassY}}, {{meshinfo.centreOfMassZ}})</p><!--3.23, 1.73, 8.15-->
        </div>
    </div>
    {% endif %}
```

## Inner structure
### CSS and Navbar on Every Page (use Flask Blueprint?)
Template location: `/templates/commons.jinja2`

I want Luxi Sans font!
```html
<style>
@font-face {
  font-family: Luxi Sans;
  src: url(/fonts/luxir.ttf);
}
    
<!--Kozuka-like Chinese font-->
body {
    font-family: Luxi Sans;
}

.leftblock {
    left: 10px;
    width: 80%;
    text-align: left;
}

.rightblock {
    right: 10px;
    width: 80%;
    text-align: right;
}
	
.fosstraffic-header {
    border-radius: 16px;
}
</style>
<link href="/fonts/fontawesome-pro-6.1.1-web/css/all.min.css" rel="stylesheet">
```

Three tabs: 'Live Dashboard', 'Insights' and 'Account Settings'
```jinja
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="/my">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/live"><i class="fa-duotone fa-signal-stream"></i> Live Dashboard</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/insights"><i class="fa-duotone fa-eye"></i> Insights</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            <img src="{{userInfo.avatarSrc}}" /> <strong>{{userInfo.username}}</strong>
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="/accountsettings">Account settings</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="/logout">Log out</a></li>
          </ul>
        </li>
      </ul>
      <!--<form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>-->
    </div>
  </div>
</nav>
```

Icons in `<v-select></v-select>`: <https://codepen.io/seryum/pen/OBYozL>

```html
<li><a class="dropdown-item active" href="#"><img src="icons/hk.png" /> Hong Kong SAR</a></li>
<li><a class="dropdown-item" href="#"><img src="icons/hk.png" /> 香港特別行政區</a></li>
<li><a class="dropdown-item" href="#"><img src="icons/gb.png" /> United Kingdom</a></li>
```

### My Live Dashboard
API endpoint: `/my`

It is implemented using Bootstrap Cards and Parallex effect. https://getbootstrap.com/docs/5.0/components/card/

```jinja
{% for cctvInstance in cctvPagination %}
<div class="card border-dark mb-3" style="max-width: 18rem;">
  <div class="card-header">Header</div>
  <div class="card-body text-dark">
    <h5 class="card-title">{{cctvInstance.cctvLocation}}</h5>
    <h6 class="card-subtitle mb-2 text-muted"><a href="/profile/{{cctvInstance.userName}}"><img src="{{cctvInstance.avatarSrc}}" class="avatar"></class> {{cctvInstance.userName}}</a></h6>
    <p class="card-text">Video goes here</p>
  </div>
  <div class="card-footer">Privacy settings goes here: <button><i class="fa-duotone {% if cctvInstance.publicOrPrivate == 'private' %}fa-lock-keyhole{% else %}fa-earth-africa{% endif %}"></i> {{cctvInstance.publicOrPrivate}}</button></div>
</div>
{% endfor %}
```

### Public Live Dashboard
API endpoint: `/live`

It is implemented using Bootstrap Cards and Parallex effect. https://getbootstrap.com/docs/5.0/components/card/

```jinja
{% for cctvInstance in cctvPagination %}
<div class="card" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">{{cctvInstance.cctvLocation}}</h5>
    <h6 class="card-subtitle mb-2 text-muted"><a href="/profile/{{cctvInstance.userName}}"><img src="{{cctvInstance.avatarSrc}}" class="avatar"></class> {{cctvInstance.userName}}</a></h6>
    <p class="card-text">Video goes here</p>
  </div>
</div>
{% endfor %}
```

### Insights
API endpoint: `/insights`

* Find peak hours by Date / Date of Week
```jinja
<button class="btn btn-outline-success" type="submit"><i class="fa-duotone fa-car-burst"></i> Find occurences of traffic accidents</button>
```
* Identify speeding vehicles. (notifications w/ `toastr`) Send email / Twitter direct message with our connectors.
* Compute average speed over the past three weeks/six weeks/year/all-time (at the given time)
* Special weather conditions (Hazy / Rainy / under Rainstorm Signals / under Tropical Cyclone Signals)
https://www.hko.gov.hk/en/weatherAPI/doc/files/HKO_Open_Data_API_Documentation.pdf (Page 13)

https://en.m.wikipedia.org/wiki/Hong_Kong_rainstorm_warning_signals
https://en.m.wikipedia.org/wiki/Hong_Kong_tropical_cyclone_warning_signals

```html
<select name="specialWeather" id="specialWeather">
    <option value="hazy" data-image="icons/hazy.png">Hazy</option><!-- if Icon in (83, 84, 85) -->
    <option value="rainy" data-image="icons/rainy.png">Rainy (excluding light rain)</option><!-- if Icon in (63, 64, 65) -->
    <option value="rainstormAmber" data-image="icons/rainstormAmber.png">Amber Rainstorm Signal</option>
    <option value="rainstormRed" data-image="icons/rainstormRed.png">Red Rainstorm Signal</option>
    <option value="rainstormBlack" data-image="icons/rainstormBlack.png">Black Rainstorm Signal</option>
    <option value="cyclone1" data-image="icons/cyclone1.png">Tropical Cyclone Signal Number 1 (Standby)</option>
    <option value="cyclone3" data-image="icons/cyclone3.png">Tropical Cyclone Signal Number 3 (Strong Wind)</option>
    <option value="cyclone8" data-image="icons/cyclone8.png">Tropical Cyclone Signal Number 8 (Gale or Storm)</option>
</select>
```

* Public Holidays by Countries / Region

```py3
from json import loads, dumps
from urllib.request import urlopen

@app.route('/render', methods = ['POST'])
    render(data={'holidayDates': getHolidayDates()})
    
def getHolidayDates():
    v = urlopen('https://www.1823.gov.hk/common/ical/en.json')
    holidays = loads(v.read().decode(encoding='utf-8').replace('\ufeff', ''))['vcalendar'][0]['vevent']
    # Format to {'name': 'Name (YYYY-MM-DD, Www)', 'date': xx}

    # Returns a list
    holidays = [{'name': f'{e["summary"]} ({datetime.strptime(e["dtstart"][0], "%Y%m%d").strftime("%Y-%m-%d")}, {datetime.strptime(e["dtstart"][0], "%Y%m%d").strftime("%A")[:-3]})',
        'date': e['dtstart'][0]} for e in holidays]

    return holidays
```

```jinja
<p>, or, pick from the list of public holidays:</p>
<!-- picking from this list should update the calendar as well -->
<select name="publicHoliday" id="publicHoliday">
    {% for dt in holidayDates %}
    <option value="{{dt['date']}}">{{dt['name']}}</option>
    {% endfor %}
</select>
```
* Most popular vehicle type/colour `<i class="fa-duotone fa-ranking-star"></i>`

```py3
from PIL import Image
from PIL.ImageStat import Stat          # https://pillow.readthedocs.io/en/stable/reference/ImageStat.html

def findNearestColour():
    vehicleColours = {'red': 0xFF0000,
    'orange': 0xFF8000,
    'yellow': 0xFFFF00,
    'green': 0x00FF00,
    'cyan': 0x00FFFF,
    'blue': 0x0000FF,
    'violet': 0x800080,
    'magenta': 0xFF00FF,
    'pink': 0xFFC0CB,
    'brown': 0x804000,
    'white': 0xFFFFFF,
    'grey': 0x808080,
    'black': 0x000000}

    for colour in vehicleColours:
        print(colour, vehicleColours[colour])
```

(Caveat: Dominant colour may be affected by sunlight conditions! There is no way to capture vehicle colour at night.)

* Lane car count (e.g., which toll has more traffic)
* 'Metaverse' simulation (recreate traffic scene by creating 3D models from vehicle type/colour on the fly + sunlight from time of the day)

### Account Settings
API endpoint: `/accountsettings`; template location: `templates/account_settings.jinja2`

```html
    <div class="mb-3 row">
        <label for="inputDisplayName" class="col-sm-2 col-form-label">Display Name</label>
        <div class="col-sm-10">
        <input type="text" readonly class="form-control" id="inputDisplayName" value="{{userInfo['displayName']}}">
        </div>
    </div>
    <div class="mb-3 row">
        <label for="inputAvatar" class="col-sm-2 col-form-label">Avatar</label>
        <div class="col-sm-10">
        <input class="form-control" type="file" id="inputAvatar">
        </div>
    </div>
    <hr>
    <div class="mb-3 row">
      <label for="oldPassword" class="form-label">Old Password</label>
      <div class="col-sm-10">
      <input type="password" class="form-control" id="oldPassword">
      </div>
    </div>
    <div class="mb-3 row">
      <label for="newPassword" class="form-label">New Password</label>
      <div class="col-sm-10">
      <input type="password" class="form-control" id="newPassword">
      </div>
    </div>
    <div class="mb-3 row">
      <label for="newPasswordRetype" class="form-label">Retype New Password</label>
      <div class="col-sm-10">
      <input type="password" class="form-control" id="newPasswordRetype">
      </div>
    </div>
    <hr>
    <div class="mb-3 row">
      <button id="btnUpdate" type="submit" class="btn btn-primary mb-3">Update information</button>
    </div>

    <h6>Payment Information</h6>
    <p style="color: dimGray;">Secured by Braintree. Cancel anytime.</p>
```

## Roadmap
Navbar top right is the i18n-next pulldown
* pandas export locale https://github.com/SoftFeta/fosstraffic/blob/main/static/locales/en/translation.json // TODO: Include a Privacy Policy / 私隱權政策 / 隐私权政策.

Terms of Service / 使用條款 / 使用条款 (Important, Scroll to the bottom!)

`/register`

```html
<h1 class="fosstraffic-header">Account registration</h1>
<p>Please read the terms of service carefully to continue your registration.</p>
<textarea class="form-control" id="termsOfService">
== TERMS OF SERVICE ==
Last Update: 25th July, 2022

At FossTraffic, privacy is of the utmost concern. We guarantee:
FossTraffic WILL NOT GIVE YOUR DATA TO THIRD-PARTY ORGANISATIONS.

Since FossTraffic only processes nadir images, the chance of accidentally capturing faces, registration plate, and other senstive material is negligible. FossTraffic will patrol uploaded materials to check violations of our terms of service.
    
Security is also of the utmost concern and hence all FossTraffic databases are highly fortified. That being said, FossTraffic will not be responsible for any threft or loss of data.

FossTraffic WILL VISIT DATA FOR PATROL PURPOSE ONLY. By using FossTraffic, you permit FossTraffic to access any uploaded data.

In case of any loss, FossTraffic will not be responsible for insight inaccuracies.
== END ==
</textarea>

<button id="btnContinue" type="button" class="btn btn-lg btn-primary" disabled>Continue</button>

$('#termsOfService').scroll(function() {
  if ($(this).scrollTop() + $(this).height() >= $(this)[0].scrollHeight - 4) {
    $('#btnContinue').removeAttr('disabled');
  }
});

$('#btnContinue').click(function() {
fetch('/register2', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
   }).then((res) => res.json())
    .then((res) => {
      console.log('Do something');
   });
});
```
`/register2`

`/register3`
```jinja
<h1 class="fosstraffic-header">Account activation</h1>
<p>To activate your account, please check your mailbox at <strong>{{email_addr}}</strong>.</p>
```

`/activate?token=`
```jinja
<h1 class="fosstraffic-header">Account activated</h1>
<p>Hurrah! Your account has been successfully activated. You will be redirected to the live dashboard.</p>
<script>
    window.setTimeout(function(){
        window.location.href = "./live";
    }, 5000);
</script>
```

* Use youtube-dl

* Trajectory to lanes?

Container: `conda install youtube-dl -c conda-forge`
```py3
from youtube_dl import YoutubeDL

ydl = YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
r = ydl.download(['https://www.youtube.com/watch?v=cJNsHN_oMjk', 'https://www.youtube.com/watch?v=BkgJZwYV8vU', 'https://www.youtube.com/watch?v=cvW729l6xlI'])
```
* Improve baseline accuracy (trucks and motorcycles), provide ResNet-152 alternative
* Speed interpolation & tooltip
* Online street mapper (polygon annotator [[ImgLab](https://github.com/NaturalIntelligence/imglab)] on the visualisation (left); line annotator on CesiumJS (right, direction is important. Reverse geocoding by OpenStreetMaps): should be able to extract street name and city name from polyline. Expand/Shrink) **Listener on polygon/line of either side is selected**

[Self-reference](https://github.com/SoftFeta/arcgis-demo-collection/blob/bb1666ba580de00dcd478a62e5e75875ea8d1b08/traffic/lanes/coco2pickledPolygons.py)
```
// Lock ImgLab to be polygon-only
// Exports to COCO (JSON)
# Save user records to key-value store

```
```py3
# Fetch user records from key-value store
def someFlaskEndpoint():
    cocotools get binary masks of road sections
```

"Change north position"
"Drag to set the north position of this CCTV" (mousemove, mouseup)

Must point north (this is crucial for identifying the vehicle direction):

![image](https://user-images.githubusercontent.com/9071916/167075816-31f3c666-36b2-4ae4-9d98-1bb5e8c5a01a.png)
```html
<style>
  .northPointer {
    z-index: 999999;
    opacity: 0.3;
  }
</style>
<canvas class="northPointer"></canvas>
var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
ctx.strokeStyle = "indigo";
ctx.beginPath();
ctx.moveTo(canvasWidth/2, canvasHeight/2);
ctx.lineTo(canvasWidth/2, 0);
ctx.stroke();

window.northAngle = 0;
$('body').mousemove((e) => {
    // Clear canvas
    // Store the current transformation matrix
    ctx.save();

    // Use the identity matrix while clearing the canvas
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, c.width, c.height);

    // Restore the transform
    ctx.restore();
    
    // Calculate angle between cursor and centre of canvas
    // ...
    window.northAngle = ;
    
    // Draw line
});

$('body').mouseup((e) => {
    // Save to database
    fetch({'/modifyMapLine'}).then((res) => {
    });
});
```
* Make feedback mechanism workable with privileged users. Just copy the Base64 src from the active element.
  * Review Panel
```html
  <h1 class="fosstraffic-header">Review Panel</h1>
  <button id="btnLoadPrev"><i class="fa-duotone fa-chevron-left"></i> Previous</button> <button id="btnLoadNext"><i class="fa-duotone fa-chevron-right"></i> Next</button> (Enable keyboard left/right key to navigate)
  function loadPrev() {
    $('#panel').animate({
      left: '-=800'
    });
    if (!hasPrev) {
      $('#btnLoadPrev').addAttr('disabled');    // Disable prev button
    }
    $('#btnLoadNext').removeAttr('disabled');
  }

  function loadNext() {
    $('#panel').animate({
      left: '+=800'
    });
    if (!hasNext) {
      $('#btnLoadNext').addAttr('disabled');    // Disable next button
    }
    $('#btnLoadPrev').removeAttr('disabled');
  }

  $('body').keydown(function(e) {
    if (e.keyCode === 37) {    // left
      loadPrev();
    }
    else if (e.keyCode === 39) {    // right
      loadNext();
    }
  });

  $('#btnLoadPrev').click(loadPrev);
  $('#btnLoadNext').click(loadNext);
```
* Model Zoo: 1. Nadir (default), 2. Oblique

Simple three-class classifcation should auto-detect nadir/oblique. The third class is invalid, e.g., blank screen, camera covered by rain, etc. (How to generate third class image ?! Use method from Oxford)

* Flutter Client

Sync time by one-shot detection OCR (It is assumed that the provided CCTVs have on-screen timestamps.)
## Schema Design
Should be stored in Parquet format.
1. `users` collection (userID, username [for changing username], hash, salt, proOrNot, confirmedMailOrNot, lastPasswordUpdate, lastModified)
    * `signUp`
    * `signIn`
    * `confirmMail`    # Set up Dovecot or Postfix: `noreply@dord.mynetgear.com`
    ```html
    Insert `longLongToken` to database's `activateAccount` collection
    Title: FossTraffic - Account Activation
    https://askubuntu.com/questions/12917/how-to-send-mail-from-the-command-line
    <div>
        <h1>Welcome to FossTraffic</h1>
        <p>Dear <strong>{{firstName}}</strong>,</p>
        <p>Click <a href="https://www.fosstraffic.com/activate?token={{longLongToken}}" target="_blank">this link</a> to activate your account.</p>
        <p>Cheers,</p>
        <p>FossTraffic Team</p>
    </div>
    ```
    * `getUserInfo`     # This is to render the Account Settings webpage
    * `changePassword`
    * `updatePaymentInfo`
2. `cctvs` collection (cctvID, cctvname [for changing name, usually the combination of roads], userID, privacy, weatherDistrictName, cctvScale, streamUrl, lastModified)
    * `createCCTV`
    * `modifyCCTV`
    * `deleteCCTV`
3. `roadsegments` collection (segmentID, cctvID, northAngle, mask [CCTV coordinates], geoJSON [Map coordinates], lastModified)
    * `modifyPolygonMasks`
    * `getPolygonMasks`
    * `deletePolygonMasks`
    * `modifyMapLine`
    * `getMapLine`
    * `deleteMapLine`
4. `history` collection (lastModified)
    * `insertHistory`
    * `getHistoryByMinute` (this will get weather too)
5. `weather` collection (date, weatherDistrictName, weatherCode, last10min, lastModified)
    * `insertWeather`
6. `trainingsamples` collection (snapshotBase64, reporterUserID, reviewed, reviewerUserID, lastModified)
    * `insertTrainingSample`
    * `getUnreviewedTrainingSample`
    * `reviewTrainingSample`
    * `getReviewedTrainingSample`

```py3
from flask import Flask, jsonify, request, send_from_directory, abort, render_template, Response
from flask_cors import CORS
from pymongo import MongoClient

from io import BytesIO

app = Flask(__name__)
CORS(app)

myclient = MongoClient('mongodb://localhost:27017/')
db = myclient['fosstraffic']

# Declare collections
users = db['users']
# sessions = db['sessions']
cctvs = db['cctvs']
roadsegments = db['roadsegments']
history = db['history']
weather = db['weather']
trainingsamples = db['trainingsamples']

# 1. `users` collection (userID, username [for changing username], hash, salt, proOrNot, confirmedMailOrNot, lastPasswordUpdate, lastModified)
@app.route('/signUp', methods = ['POST'])
def signUp():
    # Form data
    now = datetime.now()
    users.insert({'userID': request.form['userID'],
'username': request.form['username'],
'hash': request.form['hash'],
'salt': 'TODO',
'proOrNot': request.form['proOrNot'],
'confirmedMailOrNot': request.form['confirmedMailOrNot'],
'lastPasswordUpdate': now,
'lastModified': now})
    request.json
    return jsonify({'status': 0})

@app.route('/signIn', methods = ['POST'])
def signIn():
    userID = users.find_one({'username': request.form['username']})['userID']

    # Generate Session
    sessions.insert({'userID': userID, 'sessionID': generateSession()})
    request.json

    return jsonify({'status': 0})

@app.route('/confirmMail', methods = ['POST'])
def confirmMail():
    # confirmedMailOrNot can store a long token before
    
    myquery = { 'username': request.form['username'] }
    now = datetime.now()
    newvalues = { '$set': { 'confirmedMailOrNot': True, 'lastModified': now } }

    users.update_one(myquery, newvalues)
    return jsonify({'status': 0})

@app.route('/getUserInfo', methods = ['POST'])
def getUserInfo():
    myquery = { 'username': request.form['username'] }
    now = datetime.now()
    newvalues = { '$set': { 'lastModified': now } }

    users.update_one(myquery, newvalues)
    return jsonify({'status': 0})

@app.route('/changePassword', methods = ['POST'])
def changePassword():
    myquery = { 'username': request.form['username'] }
    now = datetime.now()
    newvalues = { '$set': { 'hash': newHash, 'salt': newSalt, 'lastPasswordUpdate': now, 'lastModified': now } }

    users.update_one(myquery, newvalues)
    return jsonify({'status': 0})

@app.route('/updatePaymentInfo', methods = ['POST'])
def updatePaymentInfo():
    myquery = { 'username': request.form['username'] }
    newvalues = { '$set': { 'proOrNot': True } }

    users.update_one(myquery, newvalues)
    return jsonify({'status': 0})

# 2. `cctvs` collection (cctvID, cctvname [for changing name, usually the combination of roads], userID, privacy, weatherDistrictName, cctvScale, streamUrl, lastModified)
@app.route('/createCCTV', methods = ['POST'])
def createCCTV():
    now = datetime.now()
    cctvs.insert({'cctvID': request.form['cctvID'],
'cctvname': request.form['cctvname'],
'userID': request.form['userID'],
'privacy': request.form['privacy'],
'weatherDistrictName': request.form['weatherDistrictName'],
'cctvScale': request.form['cctvScale'],
'streamUrl': request.form['streamUrl'],
'lastModified': now})
    # Update URL? 
    return jsonify({'status': 0})

@app.route('/modifyCCTV', methods = ['POST'])
def modifyCCTV():
    myquery = { 'cctvID': request.form['cctvID'] }
    now = datetime.now()
    newvalues = { '$set': {'cctvname': request.form['cctvID'],
'userID': request.form['userID'],
'privacy': request.form['privacy'],
'weatherDistrictName': request.form['weatherDistrictName'],
'cctvScale': request.form['cctvScale'],
'streamUrl': request.form['streamUrl'],
'lastModified': now} }

    ccyvs.update_one(myquery, newvalues)
    # Update URL? 
    return jsonify({'status': 0})

@app.route('/deleteCCTV', methods = ['POST'])
def deleteCCTV():
    cctvs.delete_one({})
    return jsonify({'status': 0})

# 3. `roadsegments` collection (segmentID, cctvID, northAngle, mask [CCTV coordinates], geoJSON [Map coordinates], lastModified)
@app.route('/modifyPolygonMasks', methods = ['POST'])
def modifyPolygonMasks():
    roadsegments
    return jsonify({'status': 0})

@app.route('/getPolygonMasks', methods = ['POST'])
def getPolygonMasks():
    roadsegments
    return jsonify({'status': 0})

@app.route('/deletePolygonMasks', methods = ['POST'])
def deletePolygonMasks():
    roadsegments.delete_many({})
    return jsonify({'status': 0})

@app.route('/modifyMapLine', methods = ['POST'])
def modifyMapLine():
    roadsegments
    return jsonify({'status': 0})

@app.route('/getMapLine', methods = ['POST'])
def getMapLine():
    roadsegments.find_one({})
    return jsonify({'status': 0})

@app.route('/deleteMapLine', methods = ['POST'])
def deleteMapLine():
    roadsegments.delete_one({})
    return jsonify({'status': 0})

# 4. `history` collection (lastModified)
@app.route('/insertHistory', methods = ['POST'])
def insertHistory():
    history.insert({})
    return jsonify({'status': 0})

@app.route('/getHistoryByMinute', methods = ['POST'])
def getHistoryByMinute():    # This will get the weather too
    history.find_one({})
    weather.find_one({'date': request.form['date'],
    'weatherDistrictName': request.form['weatherDistrictName']})
    return jsonify({'status': 0})

# 5. `weather` collection (date, weatherDistrictName, weatherCode, last10min, lastModified)
@app.route('/insertWeather', methods = ['POST'])
def insertWeather():
    return jsonify({'status': 0})

# 6. `trainingsamples` collection (cctvID, snapshotBase64, reporterUserID, reviewed, reviewerUserID, lastModified)
@app.route('/insertTrainingSample', methods = ['POST'])
def insertTrainingSample():
    trainingsamples.insert({'cctvID': request.form['cctvID'],
    'snapshotBase64': request.form['snapshotBase64'],
    'reporterUserID': request.form['reporterUserID'],
    'reviewed': False})
    return jsonify({'status': 0})

@app.route('/getUnreviewedTrainingSample', methods = ['POST'])
def getUnreviewedTrainingSample():
    trainingsamples
    return jsonify({'status': 0})

@app.route('/reviewTrainingSample', methods = ['POST'])
def reviewTrainingSample():
    trainingsamples
    return jsonify({'status': 0})

@app.route('/getReviewedTrainingSample', methods = ['POST'])
def getReviewedTrainingSample():
    trainingsamples.find({'cctvID': request.form['cctvID'],
    'reviewed': True})
    return jsonify({'status': 0})
    
# 7. Favourites table on the sidebar

# 8. Insights / Queries
@app.route('/getPeakHours', methods = ['POST'])
def getPeakHours():
    pass
    
@app.route('/getSpeedingVehicles', methods = ['POST'])
def getSpeedingVehicles():
    pass
    
@app.route('/getCctvSummary', methods = ['POST'])
def getCctvSummary():
    pass

# Render templates
@app.route('/my', methods = ['GET'])
def my():
    return render_template('my.jinja2', data={})

@app.route('/live', methods = ['GET'])
def live():
    return render_template('live.jinja2', data={})
    
@app.route('/insights', methods = ['GET'])
def insights():
    return render_template('insights.jinja2', data={})
    
@app.route('/accountSettings', methods = ['GET'])
def accountSettings():
    return render_template('accountSettings.jinja2', data={})
    
if __name__ == "__main__":
    # Replace below with app.run(host='0.0.0.0', port=22888) if you don't have a SSH Certificate !!!
    app.run(host='0.0.0.0', port=2888, ssl_context=('_internal/cert.pem', '_internal/privkey.pem'))
    #app.run(host='0.0.0.0', port=2888)
```

* Categorise by description (this involves multiple models)
* Visualisation

## `main.dart` Flutter Client
```dart
import 'dart:io' show Platform;

import 'package:flutter/material.dart';
import 'package:google_mobile_ads/google_mobile_ads.dart';

import 'anchored_adaptive_example.dart';
import 'fluid_example.dart';
import 'inline_adaptive_example.dart';
import 'reusable_inline_example.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  MobileAds.instance.initialize();
  runApp(MyApp());
}

// You can also test with your own ad unit IDs by registering your device as a
// test device. Check the logs for your device's ID value.
const String testDevice = 'YOUR_DEVICE_ID';
const int maxFailedLoadAttempts = 3;

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  static final AdRequest request = AdRequest(
    keywords: <String>['foo', 'bar'],
    contentUrl: 'http://foo.com/bar.html',
    nonPersonalizedAds: true,
  );

  InterstitialAd? _interstitialAd;
  int _numInterstitialLoadAttempts = 0;

  RewardedAd? _rewardedAd;
  int _numRewardedLoadAttempts = 0;

  RewardedInterstitialAd? _rewardedInterstitialAd;
  int _numRewardedInterstitialLoadAttempts = 0;

  @override
  void initState() {
    super.initState();
    _createInterstitialAd();
    _createRewardedAd();
    _createRewardedInterstitialAd();
  }

  void _createInterstitialAd() {
    InterstitialAd.load(
        adUnitId: Platform.isAndroid
            ? 'ca-app-pub-3940256099942544/1033173712'
            : 'ca-app-pub-3940256099942544/4411468910',
        request: request,
        adLoadCallback: InterstitialAdLoadCallback(
          onAdLoaded: (InterstitialAd ad) {
            print('$ad loaded');
            _interstitialAd = ad;
            _numInterstitialLoadAttempts = 0;
            _interstitialAd!.setImmersiveMode(true);
          },
          onAdFailedToLoad: (LoadAdError error) {
            print('InterstitialAd failed to load: $error.');
            _numInterstitialLoadAttempts += 1;
            _interstitialAd = null;
            if (_numInterstitialLoadAttempts < maxFailedLoadAttempts) {
              _createInterstitialAd();
            }
          },
        ));
  }

  void _showInterstitialAd() {
    if (_interstitialAd == null) {
      print('Warning: attempt to show interstitial before loaded.');
      return;
    }
    _interstitialAd!.fullScreenContentCallback = FullScreenContentCallback(
      onAdShowedFullScreenContent: (InterstitialAd ad) =>
          print('ad onAdShowedFullScreenContent.'),
      onAdDismissedFullScreenContent: (InterstitialAd ad) {
        print('$ad onAdDismissedFullScreenContent.');
        ad.dispose();
        _createInterstitialAd();
      },
      onAdFailedToShowFullScreenContent: (InterstitialAd ad, AdError error) {
        print('$ad onAdFailedToShowFullScreenContent: $error');
        ad.dispose();
        _createInterstitialAd();
      },
    );
    _interstitialAd!.show();
    _interstitialAd = null;
  }

  void _createRewardedAd() {
    RewardedAd.load(
        adUnitId: Platform.isAndroid
            ? 'ca-app-pub-3940256099942544/5224354917'
            : 'ca-app-pub-3940256099942544/1712485313',
        request: request,
        rewardedAdLoadCallback: RewardedAdLoadCallback(
          onAdLoaded: (RewardedAd ad) {
            print('$ad loaded.');
            _rewardedAd = ad;
            _numRewardedLoadAttempts = 0;
          },
          onAdFailedToLoad: (LoadAdError error) {
            print('RewardedAd failed to load: $error');
            _rewardedAd = null;
            _numRewardedLoadAttempts += 1;
            if (_numRewardedLoadAttempts < maxFailedLoadAttempts) {
              _createRewardedAd();
            }
          },
        ));
  }

  void _showRewardedAd() {
    if (_rewardedAd == null) {
      print('Warning: attempt to show rewarded before loaded.');
      return;
    }
    _rewardedAd!.fullScreenContentCallback = FullScreenContentCallback(
      onAdShowedFullScreenContent: (RewardedAd ad) =>
          print('ad onAdShowedFullScreenContent.'),
      onAdDismissedFullScreenContent: (RewardedAd ad) {
        print('$ad onAdDismissedFullScreenContent.');
        ad.dispose();
        _createRewardedAd();
      },
      onAdFailedToShowFullScreenContent: (RewardedAd ad, AdError error) {
        print('$ad onAdFailedToShowFullScreenContent: $error');
        ad.dispose();
        _createRewardedAd();
      },
    );

    _rewardedAd!.setImmersiveMode(true);
    _rewardedAd!.show(
        onUserEarnedReward: (AdWithoutView ad, RewardItem reward) {
      print('$ad with reward $RewardItem(${reward.amount}, ${reward.type})');
    });
    _rewardedAd = null;
  }

  void _createRewardedInterstitialAd() {
    RewardedInterstitialAd.load(
        adUnitId: Platform.isAndroid
            ? 'ca-app-pub-3940256099942544/5354046379'
            : 'ca-app-pub-3940256099942544/6978759866',
        request: request,
        rewardedInterstitialAdLoadCallback: RewardedInterstitialAdLoadCallback(
          onAdLoaded: (RewardedInterstitialAd ad) {
            print('$ad loaded.');
            _rewardedInterstitialAd = ad;
            _numRewardedInterstitialLoadAttempts = 0;
          },
          onAdFailedToLoad: (LoadAdError error) {
            print('RewardedInterstitialAd failed to load: $error');
            _rewardedInterstitialAd = null;
            _numRewardedInterstitialLoadAttempts += 1;
            if (_numRewardedInterstitialLoadAttempts < maxFailedLoadAttempts) {
              _createRewardedInterstitialAd();
            }
          },
        ));
  }

  void _showRewardedInterstitialAd() {
    if (_rewardedInterstitialAd == null) {
      print('Warning: attempt to show rewarded interstitial before loaded.');
      return;
    }
    _rewardedInterstitialAd!.fullScreenContentCallback =
        FullScreenContentCallback(
      onAdShowedFullScreenContent: (RewardedInterstitialAd ad) =>
          print('$ad onAdShowedFullScreenContent.'),
      onAdDismissedFullScreenContent: (RewardedInterstitialAd ad) {
        print('$ad onAdDismissedFullScreenContent.');
        ad.dispose();
        _createRewardedInterstitialAd();
      },
      onAdFailedToShowFullScreenContent:
          (RewardedInterstitialAd ad, AdError error) {
        print('$ad onAdFailedToShowFullScreenContent: $error');
        ad.dispose();
        _createRewardedInterstitialAd();
      },
    );

    _rewardedInterstitialAd!.setImmersiveMode(true);
    _rewardedInterstitialAd!.show(
        onUserEarnedReward: (AdWithoutView ad, RewardItem reward) {
      print('$ad with reward $RewardItem(${reward.amount}, ${reward.type})');
    });
    _rewardedInterstitialAd = null;
  }

  @override
  void dispose() {
    super.dispose();
    _interstitialAd?.dispose();
    _rewardedAd?.dispose();
    _rewardedInterstitialAd?.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Builder(builder: (BuildContext context) {
        return Scaffold(
          appBar: AppBar(
            title: const Text('AdMob Plugin example app'),
            actions: <Widget>[
              PopupMenuButton<String>(
                onSelected: (String result) {
                  switch (result) {
                    case 'InterstitialAd':
                      _showInterstitialAd();
                      break;
                    case 'RewardedAd':
                      _showRewardedAd();
                      break;
                    case 'RewardedInterstitialAd':
                      _showRewardedInterstitialAd();
                      break;
                    case 'Fluid':
                      Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => FluidExample()),
                      );
                      break;
                    case 'Inline adaptive':
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                            builder: (context) => InlineAdaptiveExample()),
                      );
                      break;
                    case 'Anchored adaptive':
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                            builder: (context) => AnchoredAdaptiveExample()),
                      );
                      break;
                    default:
                      throw AssertionError('unexpected button: $result');
                  }
                },
                itemBuilder: (BuildContext context) => <PopupMenuEntry<String>>[
                  PopupMenuItem<String>(
                    value: 'InterstitialAd',
                    child: Text('InterstitialAd'),
                  ),
                  PopupMenuItem<String>(
                    value: 'RewardedAd',
                    child: Text('RewardedAd'),
                  ),
                  PopupMenuItem<String>(
                    value: 'RewardedInterstitialAd',
                    child: Text('RewardedInterstitialAd'),
                  ),
                  PopupMenuItem<String>(
                    value: 'Fluid',
                    child: Text('Fluid'),
                  ),
                  PopupMenuItem<String>(
                    value: 'Inline adaptive',
                    child: Text('Inline adaptive'),
                  ),
                  PopupMenuItem<String>(
                    value: 'Anchored adaptive',
                    child: Text('Anchored adaptive'),
                  ),
                ],
              ),
            ],
          ),
          body: SafeArea(child: ReusableInlineExample()),
        );
      }),
    );
  }
}
```

* https://github.com/NearHuscarl/flutter_login
* https://flutter.dev/monetization
* https://pub.dev/packages/google_mobile_ads/example (does NOT support web unfortunately)<p>The Google Mobile Ads SDK for Flutter works with both AdMob and Ad Manager. It is the first step towards supporting a variety of ad formats, including banner, interstitial, rewarded video, and native ads to earn revenue.</p>

## `PrivacyPolicy.vue` Legal
* CesiumJS, use under Apache licence (https://github.com/CesiumGS/cesium/blob/main/LICENSE.md)
