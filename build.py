#!/usr/bin/env python3
"""
Generates the CBTWeb static pages from shared header/footer partials +
per-page content. Plain output, no server include needed — run this
whenever a page is added/changed, then commit the generated .html files
(the .html files are what actually gets deployed/served).
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
PHONE = "(804) 521-7660"
PHONE_TEL = "+18045217660"
EMAIL = "hello@codebluetechnology.com"

NAV_SOLUTIONS = [
    ("Managed IT & PeopleFirst Support", "managed-it.html"),
    ("Cyber Security", "cyber-security.html"),
    ("Cloud & Data Center Hosting", "data-center.html"),
    ("Voice / VoIP", "voip.html"),
    ("Data Cabling", "data-cabling.html"),
    ("Premise Security & Cameras", "premise-security.html"),
]

TOP_NAV = [
    ("PeopleFirst Support", "peoplefirst-support.html"),
    ("Industries", "industries.html"),
    ("About", "about.html"),
    ("Resources", "resources.html"),
    ("Careers", "careers.html"),
]

def head(title, description, active=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="css/styles.css">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "CodeBlue Technology",
  "telephone": "{PHONE}",
  "email": "{EMAIL}",
  "areaServed": "Central Virginia",
  "location": [
    {{"@type":"Place","address":{{"@type":"PostalAddress","streetAddress":"9204 Center Oak Court STE C","addressLocality":"Mechanicsville","addressRegion":"VA","postalCode":"23116"}}}},
    {{"@type":"Place","address":{{"@type":"PostalAddress","streetAddress":"5020 Richmond Rd STE A","addressLocality":"Warsaw","addressRegion":"VA","postalCode":"22572"}}}}
  ]
}}
</script>
</head>
<body>
"""

def header(active=""):
    mega_items = "\n".join(
        f'      <a href="{href}">{label}</a>' for label, href in NAV_SOLUTIONS
    )
    top_items_parts = []
    for label, href in TOP_NAV:
        current = ' aria-current="page"' if href == active else ""
        top_items_parts.append(
            '  <div class="nav-item"><a class="nav-link" href="%s"%s>%s</a></div>' % (href, current, label)
        )
    top_items = "\n".join(top_items_parts)
    mobile_solutions = "\n".join(
        f'      <a class="sub-link" href="{href}">{label}</a>' for label, href in NAV_SOLUTIONS
    )
    mobile_top = "\n".join(
        f'    <a href="{href}">{label}</a>' for label, href in TOP_NAV
    )
    return f"""<a href="#main" class="visually-hidden">Skip to content</a>
<header class="site-header">
  <div class="container">
    <a href="index.html" class="brand"><span class="dot"></span> CodeBlue Technology</a>
    <nav class="nav-desktop" aria-label="Primary">
      <div class="nav-item has-mega">
        <a class="nav-link" href="managed-it.html">Solutions</a>
        <div class="mega-menu">
{mega_items}
        </div>
      </div>
{top_items}
    </nav>
    <div class="header-actions">
      <a class="header-phone" href="tel:{PHONE_TEL}">{PHONE}</a>
      <a class="btn btn-primary" href="contact.html">Talk to a Rep</a>
      <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false"><span></span></button>
    </div>
  </div>
  <div class="nav-mobile">
    <div class="container">
      <details open>
        <summary>Solutions</summary>
{mobile_solutions}
      </details>
{mobile_top}
      <a href="contact.html" style="margin-top:10px;">Contact</a>
    </div>
  </div>
</header>
"""

def footer():
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <h4>CodeBlue Technology</h4>
        <p style="color:rgba(255,255,255,0.65); max-width:34ch;">Founded 2003 in Richmond, VA. 550+ active clients across Central Virginia and the Northern Neck. Managed IT, cyber security, data cabling, VoIP, and premise security &mdash; support that follows your team, not your equipment.</p>
        <div class="footer-social">
          <a href="#">Facebook</a><a href="#">LinkedIn</a><a href="#">Instagram</a><a href="#">Podcast</a>
        </div>
      </div>
      <div>
        <h4>Solutions</h4>
        <ul>
          {"".join(f'<li><a href="{href}">{label}</a></li>' for label, href in NAV_SOLUTIONS)}
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="about.html">About</a></li>
          <li><a href="industries.html">Industries</a></li>
          <li><a href="resources.html">Resources</a></li>
          <li><a href="careers.html">Careers</a></li>
        </ul>
      </div>
      <div>
        <h4>Get in Touch</h4>
        <ul>
          <li><a href="tel:{PHONE_TEL}">Richmond: {PHONE}</a></li>
          <li><a href="tel:+18044564500">Warsaw: (804) 456-4500</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="contact.html">Contact page</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span id="year"></span> CodeBlue Technology. All rights reserved.</span>
      <span>Richmond, VA &middot; Warsaw, VA</span>
    </div>
  </div>
</footer>
<div class="call-bar">
  <a href="tel:{PHONE_TEL}">&#128222; Call {PHONE}</a>
  <a href="sms:{PHONE_TEL}">&#128172; Text Us</a>
</div>
<script src="js/main.js"></script>
<script>document.getElementById("year").textContent = new Date().getFullYear();</script>
</body>
</html>
"""

def rep_form(context="this"):
    return f"""<div class="rep-form animate-in">
  <h3>Talk to a Rep</h3>
  <p class="sub">A CodeBlue rep will call, text, or email you within 1 business hour.</p>
  <form>
    <div class="field">
      <label for="rf-name">Name</label>
      <input id="rf-name" type="text" required placeholder="Your name">
    </div>
    <div class="field">
      <label for="rf-contact">Phone or Email</label>
      <input id="rf-contact" type="text" required placeholder="Best way to reach you">
    </div>
    <div class="field">
      <label for="rf-need">What do you need help with?</label>
      <select id="rf-need">
        <option>Managed IT / PeopleFirst Support</option>
        <option>Cyber Security</option>
        <option>Cloud &amp; Data Center Hosting</option>
        <option>Voice / VoIP</option>
        <option>Data Cabling</option>
        <option>Premise Security &amp; Cameras</option>
        <option>Not sure yet</option>
      </select>
    </div>
    <button type="submit" class="btn btn-primary btn-block">Send &amp; Get a Callback</button>
  </form>
  <div class="form-confirm">A CodeBlue rep will call, text, or email you within 1 business hour. Prefer to talk now? Call {PHONE}.</div>
  <p class="form-note">Want to pre-qualify yourself in more detail first? <a href="contact.html#full-form">Use the full form instead &rarr;</a></p>
</div>"""

def proof_bar():
    return """<div class="proof-bar">
  <div class="container">
    <ul>
      <li><strong>2003</strong> Founded in Richmond, VA</li>
      <li><strong>550+</strong> Active clients</li>
      <li><strong>20+ yrs</strong> Central Virginia trust</li>
      <li><strong>DCJS</strong> Licensed security techs</li>
    </ul>
  </div>
</div>"""

def write(path, html):
    with open(os.path.join(ROOT, path), "w") as f:
        f.write(html)
    print("wrote", path)

# ---------------------------------------------------------------------------
# HOMEPAGE
# ---------------------------------------------------------------------------
home = head(
    "CodeBlue Technology | Managed IT, Cyber Security & Support in Richmond, VA",
    "Support that follows your team, not your equipment. Managed IT, cyber security, VoIP, data cabling and premise security for Central Virginia businesses since 2003."
) + header("index.html") + f"""
<main id="main">
<section class="hero">
  <div class="container">
    <div>
      <span class="eyebrow" style="color:#8fc2ff;">Central Virginia's IT Partner Since 2003</span>
      <h1>Support that follows your team, not your equipment.</h1>
      <p class="lead">Managed IT, cyber security, VoIP, data cabling, and premise security for 550+ businesses across Richmond and the Northern Neck &mdash; with a single rep who actually knows your team.</p>
      <div class="hero-ctas">
        <a href="contact.html" class="btn btn-primary">Talk to a Rep</a>
        <a href="peoplefirst-support.html" class="btn btn-outline">See PeopleFirst Support</a>
      </div>
    </div>
    <div class="hero-art">Hero visual: team photo or product screenshot placeholder</div>
  </div>
</section>

{proof_bar()}

<section class="section">
  <div class="container">
    <div class="section-head center">
      <div class="divider"></div>
      <span class="eyebrow">Solutions</span>
      <h2>Everything your business needs to run on secure, reliable technology</h2>
    </div>
    <div class="grid grid-3">
      <a class="card" href="managed-it.html"><div class="icon">IT</div><h3>Managed IT &amp; PeopleFirst Support</h3><p>Flat per-person pricing that covers every device, vendor and cyber tool your team touches.</p></a>
      <a class="card" href="cyber-security.html"><div class="icon">CS</div><h3>Cyber Security</h3><p>Endpoint protection, phishing training, and 24/7 threat monitoring built into every plan.</p></a>
      <a class="card" href="data-center.html"><div class="icon">DC</div><h3>Cloud &amp; Data Center Hosting</h3><p>Private and public cloud, failover, and SOC II-compliant hosting.</p></a>
      <a class="card" href="voip.html"><div class="icon">VP</div><h3>Voice / VoIP</h3><p>Cloud and premise voice systems, SIP trunking, and call center solutions.</p></a>
      <a class="card" href="data-cabling.html"><div class="icon">DC</div><h3>Data Cabling</h3><p>DCJS-licensed structured cabling and infrastructure builds.</p></a>
      <a class="card" href="premise-security.html"><div class="icon">PS</div><h3>Premise Security &amp; Cameras</h3><p>Access control and camera systems, monitored and maintained.</p></a>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="grid grid-2" style="align-items:center;">
      <div>
        <span class="eyebrow">Flagship Offer</span>
        <h2>PeopleFirst Support: IT priced around your people, not your devices</h2>
        <p>One flat rate per team member covers hardware, software, third-party vendor support, and cyber security &mdash; on-site and remote. No surprise device bills, no gaps in coverage.</p>
        <a href="peoplefirst-support.html" class="btn btn-outline-navy">How PeopleFirst works &rarr;</a>
      </div>
      <div class="card">
        <h3>What's included</h3>
        <ul>
          <li>Hardware &amp; software support</li>
          <li>Third-party vendor support</li>
          <li>Cyber security tools &amp; training</li>
          <li>On-site + remote coverage</li>
          <li>A dedicated Client Advocate</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center">
      <div class="divider"></div>
      <span class="eyebrow">Industries</span>
      <h2>Built for the way your industry actually works</h2>
    </div>
    <div class="chip-row" style="justify-content:center;">
      <a class="chip" href="industries.html">Healthcare</a>
      <a class="chip" href="industries.html">Legal</a>
      <a class="chip" href="industries.html">Financial Services</a>
      <a class="chip" href="industries.html">Dental</a>
      <a class="chip" href="industries.html">Automotive</a>
      <a class="chip" href="industries.html">Government</a>
      <a class="chip" href="industries.html">Hospitality</a>
      <a class="chip" href="industries.html">Retail</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-band">
      <h2>Let's get started together.</h2>
      <p>Tell us what you need and a rep will follow up within 1 business hour.</p>
      <div class="hero-ctas">
        <a href="contact.html" class="btn btn-primary">Talk to a Rep</a>
        <a href="tel:{PHONE_TEL}" class="btn btn-outline">Call {PHONE}</a>
      </div>
    </div>
  </div>
</section>
</main>
""" + footer()
write("index.html", home)

# ---------------------------------------------------------------------------
# MANAGED IT (pillar/service page TEMPLATE example)
# ---------------------------------------------------------------------------
managed_it = head(
    "Managed IT Services in Richmond, VA | CodeBlue Technology",
    "Flat-rate managed IT support for Central Virginia businesses. Hardware, software, vendor and cyber security support in one plan."
) + header("managed-it.html") + f"""
<main id="main">
<section class="hero">
  <div class="container">
    <div>
      <span class="eyebrow" style="color:#8fc2ff;">Managed IT Services</span>
      <h1>IT support that actually knows your business.</h1>
      <p class="lead">Flat-rate managed IT for growing teams &mdash; proactive monitoring, a real help desk, and a plan built around how your people actually work.</p>
      <div class="hero-ctas">
        <a href="contact.html" class="btn btn-primary">Talk to a Rep</a>
        <a href="peoplefirst-support.html" class="btn btn-outline">Compare with PeopleFirst</a>
      </div>
    </div>
    <div class="hero-art">Hero visual placeholder</div>
  </div>
</section>

{proof_bar()}

<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="divider"></div>
      <span class="eyebrow">What's Included</span>
      <h2>Everything your team needs to stay online and secure</h2>
    </div>
    <div class="grid grid-4">
      <div class="card"><div class="icon">1</div><h3>Help Desk</h3><p>Unlimited remote &amp; on-site support.</p></div>
      <div class="card"><div class="icon">2</div><h3>Monitoring</h3><p>24/7 proactive monitoring of every endpoint.</p></div>
      <div class="card"><div class="icon">3</div><h3>Patching</h3><p>OS and third-party patch management.</p></div>
      <div class="card"><div class="icon">4</div><h3>Vendor Mgmt</h3><p>We call your vendors so you don't have to.</p></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <div class="divider"></div>
      <span class="eyebrow">How It Works</span>
      <h2>Onboarding without the disruption</h2>
    </div>
    <div class="steps">
      <div class="step"><div class="num"></div><div><h3>Assessment</h3><p>We inventory your environment and flag risks before day one.</p></div></div>
      <div class="step"><div class="num"></div><div><h3>Onboarding</h3><p>Agents deployed, backups configured, vendors contacted &mdash; on a schedule that doesn't interrupt your team.</p></div></div>
      <div class="step"><div class="num"></div><div><h3>Ongoing Support</h3><p>A dedicated point of contact and monthly reporting from day one.</p></div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-2" style="align-items:start;">
      <div>
        <div class="section-head">
          <div class="divider"></div>
          <span class="eyebrow">Related</span>
          <h2>See how PeopleFirst reframes IT around your people</h2>
        </div>
        <p>Managed IT can be priced per-device or per-person. Our PeopleFirst model covers every device a team member uses under one flat rate.</p>
        <a href="peoplefirst-support.html" class="btn btn-outline-navy">Explore PeopleFirst Support &rarr;</a>
        <div class="chip-row" style="margin-top:24px;">
          <a class="chip" href="industries.html">Healthcare</a>
          <a class="chip" href="industries.html">Legal</a>
          <a class="chip" href="industries.html">Financial Services</a>
        </div>
      </div>
      {rep_form()}
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="cta-band">
      <h2>Ready to stop firefighting IT?</h2>
      <p>Get a straight answer on what managed IT should cost for your team.</p>
      <div class="hero-ctas">
        <a href="contact.html" class="btn btn-primary">Talk to a Rep</a>
      </div>
    </div>
  </div>
</section>
</main>
""" + footer()
write("managed-it.html", managed_it)

# ---------------------------------------------------------------------------
# PEOPLEFIRST SUPPORT (flagship page)
# ---------------------------------------------------------------------------
peoplefirst = head(
    "PeopleFirst Support | Per-Person IT Support | CodeBlue Technology",
    "PeopleFirst Support is CodeBlue's flat per-person IT plan: hardware, software, third-party vendor and cyber security support, on-site and remote."
) + header("peoplefirst-support.html") + f"""
<main id="main">
<section class="hero">
  <div class="container">
    <div>
      <span class="eyebrow" style="color:#8fc2ff;">Flagship Offer</span>
      <h1>Support that follows your team, not your equipment.</h1>
      <p class="lead">One flat rate per person &mdash; not per device. PeopleFirst Support covers everything a team member touches: hardware, software, vendors, and cyber security, on-site and remote.</p>
      <div class="hero-ctas">
        <a href="contact.html" class="btn btn-primary">Talk to a Rep</a>
        <a href="#pricing" class="btn btn-outline">How pricing works</a>
      </div>
    </div>
    <div class="hero-art">Hero visual placeholder</div>
  </div>
</section>

{proof_bar()}

<section class="section" id="pricing">
  <div class="container">
    <div class="section-head">
      <div class="divider"></div>
      <span class="eyebrow">How Pricing Works</span>
      <h2>Plain-language pricing, no per-device math</h2>
    </div>
    <p style="max-width:60ch;">Most IT plans price per device &mdash; the more laptops, phones, and servers your team uses, the higher the bill, no matter how it's used. PeopleFirst flips that: every enrolled team member gets one flat monthly rate that covers every device and tool they touch. Enroll your whole staff and the math gets simpler, not more expensive.</p>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <div class="divider"></div>
      <span class="eyebrow">What's Included</span>
      <h2>Four things, covered for every person</h2>
    </div>
    <div class="grid grid-4">
      <div class="card"><div class="icon">1</div><h3>Hardware Support</h3><p>Every device your team member uses, covered.</p></div>
      <div class="card"><div class="icon">2</div><h3>Software Support</h3><p>Installs, updates, and troubleshooting included.</p></div>
      <div class="card"><div class="icon">3</div><h3>3rd-Party Vendor Support</h3><p>We're the ones on hold with your vendors.</p></div>
      <div class="card"><div class="icon">4</div><h3>Cyber Security</h3><p>Endpoint protection and training built in.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="divider"></div>
      <span class="eyebrow">Behind the Tech</span>
      <h2>A Client Advocate who actually knows your team</h2>
    </div>
    <p style="max-width:60ch;">Every PeopleFirst account gets a dedicated Client Advocate &mdash; a real point of contact who knows your environment, tracks recurring issues, and escalates on your behalf instead of routing you through a ticket queue.</p>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head center">
      <div class="divider"></div>
      <span class="eyebrow">Old vs. New</span>
      <h2>People-based vs. device/license-based support</h2>
    </div>
    <div class="grid grid-2">
      <div class="card">
        <h3>Device/License-Based (old model)</h3>
        <ul>
          <li>Price grows with every device added</li>
          <li>Coverage gaps between devices and licenses</li>
          <li>Vendor issues are your problem to chase</li>
        </ul>
      </div>
      <div class="card" style="border-color:var(--sky); box-shadow:var(--shadow-lg);">
        <h3>PeopleFirst (per-person)</h3>
        <ul>
          <li>One flat rate per team member</li>
          <li>Every device that person uses is covered</li>
          <li>We manage vendors on your behalf</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-2" style="align-items:start;">
      <div class="card">
        <h3>PeopleFirst Support Guide</h3>
        <p>Download the full breakdown of what's included, how enrollment works, and real client examples.</p>
        <a href="resources.html" class="btn btn-outline-navy">Get the PDF &rarr;</a>
      </div>
      {rep_form()}
    </div>
  </div>
</section>
</main>
""" + footer()
write("peoplefirst-support.html", peoplefirst)

# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------
about = head(
    "About CodeBlue Technology | Richmond, VA Managed IT Provider",
    "Founded in 2003 in Richmond, VA. CodeBlue Technology serves 550+ businesses across Central Virginia with managed IT, cyber security, and more."
) + header("about.html") + f"""
<main id="main">
<section class="hero">
  <div class="container">
    <div>
      <span class="eyebrow" style="color:#8fc2ff;">About Us</span>
      <h1>20+ years of keeping Central Virginia businesses running.</h1>
      <p class="lead">Founded in 2003 and based in Richmond, VA, CodeBlue Technology has grown alongside the businesses we serve &mdash; now supporting 550+ active clients across Richmond and the Northern Neck.</p>
    </div>
    <div class="hero-art">Team / office photo placeholder</div>
  </div>
</section>

{proof_bar()}

<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="divider"></div>
      <span class="eyebrow">Our Story</span>
      <h2>Started local, stayed local</h2>
    </div>
    <p style="max-width:65ch;">CodeBlue Technology was founded in Richmond, Virginia in 2003 by Trey Hayden. What started as a small IT support shop has grown into a full-service technology partner with offices in Mechanicsville and Warsaw, VA &mdash; without losing the personal, know-your-name relationship that got us here.</p>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="grid grid-2">
      <div class="card">
        <h3>Richmond Office</h3>
        <p>9204 Center Oak Court STE C<br>Mechanicsville, VA 23116<br><a href="tel:+18045217660">(804) 521-7660</a></p>
      </div>
      <div class="card">
        <h3>Northern Neck Office</h3>
        <p>5020 Richmond Rd STE A<br>Warsaw, VA 22572<br><a href="tel:+18044564500">(804) 456-4500</a></p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-band">
      <h2>Become a Partner</h2>
      <p>Let's get started together &mdash; talk to a rep about your team's technology needs.</p>
      <div class="hero-ctas">
        <a href="contact.html" class="btn btn-primary">Talk to a Rep</a>
      </div>
    </div>
  </div>
</section>
</main>
""" + footer()
write("about.html", about)

# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------
contact = head(
    "Contact CodeBlue Technology | Richmond & Warsaw, VA",
    "Get in touch with CodeBlue Technology. Call, text, or send a message and a rep will follow up within 1 business hour."
) + header("contact.html") + f"""
<main id="main">
<section class="section" style="padding-top:44px;">
  <div class="container">
    <div class="section-head center">
      <div class="divider"></div>
      <span class="eyebrow">Contact</span>
      <h1>Let's get started together.</h1>
      <p>Call, text, or send a quick message &mdash; a CodeBlue rep will respond within 1 business hour.</p>
    </div>
    <div class="grid grid-2" style="align-items:start; max-width:900px; margin:0 auto;">
      {rep_form()}
      <div class="card">
        <h3>Prefer to reach us directly?</h3>
        <p><strong>Richmond:</strong> <a href="tel:+18045217660">(804) 521-7660</a><br>
        <strong>Warsaw:</strong> <a href="tel:+18044564500">(804) 456-4500</a><br>
        <strong>Email:</strong> <a href="mailto:hello@codebluetechnology.com">hello@codebluetechnology.com</a><br>
        <strong>Service requests:</strong> <a href="mailto:service@codebluetechnology.com">service@codebluetechnology.com</a></p>
        <p id="full-form" style="margin-top:20px;">Want to pre-qualify yourself with more detail before a rep calls? The full intake form is available as a secondary option &mdash; ask your rep for the link, or we'll add a dedicated long-form page here.</p>
      </div>
    </div>
  </div>
</section>
</main>
""" + footer()
write("contact.html", contact)

# ---------------------------------------------------------------------------
# PLACEHOLDER PAGES (kept live so nav never 404s; fill in next)
# ---------------------------------------------------------------------------
placeholders = {
    "cyber-security.html": ("Cyber Security", "Endpoint protection, phishing training, and 24/7 threat monitoring for Central Virginia businesses."),
    "data-center.html": ("Cloud & Data Center Hosting", "Private and public cloud hosting, failover, and SOC II-compliant data center services."),
    "voip.html": ("Voice / VoIP", "Cloud and premise voice systems, SIP trunking, call center and conference room solutions."),
    "data-cabling.html": ("Data Cabling", "DCJS-licensed structured cabling and network infrastructure for Central Virginia businesses."),
    "premise-security.html": ("Premise Security & Cameras", "Access control and camera systems, monitored and maintained by CodeBlue Technology."),
    "industries.html": ("Industries We Serve", "CodeBlue Technology serves healthcare, legal, financial services, dental, automotive, government, hospitality, and retail businesses."),
    "resources.html": ("Resources", "Guides, checklists, and downloads from CodeBlue Technology."),
    "careers.html": ("Careers", "Join the CodeBlue Technology team in Richmond, VA."),
}
for slug, (title, desc) in placeholders.items():
    page = head(f"{title} | CodeBlue Technology", desc) + header(slug) + f"""
<main id="main">
<section class="hero">
  <div class="container">
    <div>
      <span class="eyebrow" style="color:#8fc2ff;">Coming Soon</span>
      <h1>{title}</h1>
      <p class="lead">{desc} This page is being rebuilt as part of the new site &mdash; full content coming next.</p>
      <div class="hero-ctas">
        <a href="contact.html" class="btn btn-primary">Talk to a Rep</a>
      </div>
    </div>
  </div>
</section>
{proof_bar()}
</main>
""" + footer()
    write(slug, page)

print("\nDone.")
