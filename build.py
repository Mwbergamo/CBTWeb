#!/usr/bin/env python3
"""
Generates the CBTWeb static pages from shared header/footer partials +
per-page content. Plain output, no server include needed - run this
whenever a page is added/changed, then commit the generated .html files
(the .html files are what actually gets deployed/served).

Design system v3: brushed aluminum + frosted glass, brand palette from
PMS 281 C / 377 C / 202 C. See css/styles.css for the token system.
Copy rule: no em dashes, ever.
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

def head(title, description):
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
    mega_items = "\n".join(f'      <a href="{href}">{label}</a>' for label, href in NAV_SOLUTIONS)
    top_items_parts = []
    for label, href in TOP_NAV:
        current = ' aria-current="page"' if href == active else ""
        top_items_parts.append(f'  <div class="nav-item"><a class="nav-link" href="{href}"{current}>{label}</a></div>')
    top_items = "\n".join(top_items_parts)
    mobile_solutions = "\n".join(f'      <a class="sub-link" href="{href}">{label}</a>' for label, href in NAV_SOLUTIONS)
    mobile_top = "\n".join(f'    <a href="{href}">{label}</a>' for label, href in TOP_NAV)
    return f"""<a href="#main" class="visually-hidden">Skip to content</a>
<header class="site-header">
  <div class="container">
    <a href="index.html" class="brand"><span class="mark"></span> CodeBlue Technology</a>
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
      <a class="header-phone mono" href="tel:{PHONE_TEL}">{PHONE}</a>
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
        <p style="color:rgba(246,245,242,0.62); max-width:34ch;">Founded 2003 in Richmond, VA. 550+ active clients across Central Virginia and the Northern Neck. Managed IT, cyber security, data cabling, VoIP, and premise security. Support that follows your team, not your equipment.</p>
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
  <a href="tel:{PHONE_TEL}">Call {PHONE}</a>
  <a href="sms:{PHONE_TEL}">Text Us</a>
</div>
<script src="js/main.js"></script>
<script>document.getElementById("year").textContent = new Date().getFullYear();</script>
</body>
</html>
"""

def rep_form():
    return f"""<div class="rep-form card reveal">
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
  <p class="form-note">Want more detail before a rep calls? <a href="contact.html#full-form">Use the full form instead.</a></p>
</div>"""

def stat_strip():
    return """<div class="stat-strip">
  <div class="container">
    <ul>
      <li><strong class="mono">2003</strong><span>Founded in Richmond, VA</span></li>
      <li><strong class="mono">550+</strong><span>Active clients</span></li>
      <li><strong class="mono">20+</strong><span>Years in Central Virginia</span></li>
      <li><strong class="mono">DCJS</strong><span>Licensed security techs</span></li>
    </ul>
  </div>
</div>"""

_panel_seed = [0]

def hero(eyebrow, h1, lead, ctas, icon="network"):
    eyebrow_html = f'<span class="label">{eyebrow}</span>' if eyebrow else ""
    _panel_seed[0] += 1
    return f"""<section class="hero">
  <div class="container">
    <div class="hero-inner">
      <div class="hero-grid">
        <div class="hero-copy">
          {eyebrow_html}
          <h1>{h1}</h1>
          <p class="lead">{lead}</p>
          <div class="hero-ctas">{ctas}</div>
        </div>
        <div class="hero-media">
          {material_panel(icon, _panel_seed[0])}
        </div>
      </div>
    </div>
  </div>
</section>"""

ICON_PATHS = {
    # simple geometric line-marks, drawn to fit a 120x120 box centered
    "network": '<circle cx="60" cy="30" r="9"/><circle cx="30" cy="90" r="9"/><circle cx="90" cy="90" r="9"/><path d="M60 39 L36 82 M60 39 L84 82 M39 90 L81 90"/>',
    "people": '<circle cx="45" cy="42" r="18"/><circle cx="78" cy="52" r="14"/><path d="M18 96c0-16 12-27 27-27s27 11 27 27M60 96c2-13 11-21 24-21s24 8 24 21"/>',
    "shield": '<path d="M60 14 L98 28 V58 C98 82 82 96 60 106 C38 96 22 82 22 58 V28 Z"/><path d="M42 58 L54 70 L80 44"/>',
    "building": '<rect x="30" y="20" width="60" height="86" rx="2"/><path d="M42 36h10M68 36h10M42 54h10M68 54h10M42 72h10M68 72h10M50 106V88h20v18"/>',
}

def material_panel(icon="network", seed=0):
    """Inline SVG: brushed aluminum ground, a brand blue-to-green accent
    strip, and a frosted-glass roundel holding a simple line mark. No
    network dependency, no stock photography; the material language *is*
    the image."""
    icon_paths = ICON_PATHS.get(icon, ICON_PATHS["network"])
    # slight per-instance offset so repeated panels don't look identical
    offset = (seed * 37) % 90
    return f"""<svg class="material-panel" viewBox="0 0 900 700" preserveAspectRatio="xMidYMid slice" role="img" aria-hidden="true">
  <defs>
    <linearGradient id="alu-{seed}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="var(--alu-100)"/>
      <stop offset="55%" stop-color="var(--alu-200)"/>
      <stop offset="100%" stop-color="var(--alu-300)"/>
    </linearGradient>
    <linearGradient id="brand-strip-{seed}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="var(--brand-blue)"/>
      <stop offset="100%" stop-color="var(--brand-green)"/>
    </linearGradient>
    <pattern id="brush-{seed}" width="6" height="6" patternTransform="rotate(8)" patternUnits="userSpaceOnUse">
      <rect width="6" height="6" fill="transparent"/>
      <line x1="0" y1="0" x2="0" y2="6" stroke="rgba(0,0,0,0.05)" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="900" height="700" fill="url(#alu-{seed})"/>
  <rect width="900" height="700" fill="url(#brush-{seed})"/>
  <rect x="{-40 + offset}" y="560" width="1000" height="46" fill="url(#brand-strip-{seed})" opacity="0.9" transform="rotate(-3 450 580)"/>
  <circle cx="450" cy="330" r="168" fill="rgba(255,255,255,0.32)" stroke="rgba(255,255,255,0.55)" stroke-width="1.5"/>
  <circle cx="450" cy="330" r="168" fill="none" stroke="var(--line)" stroke-width="1"/>
  <g transform="translate(390 270)" fill="none" stroke="var(--brand-green-deep)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
    {icon_paths}
  </g>
</svg>"""

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
{hero(
    "Central Virginia, since 2003",
    "Support that follows your team, not your equipment.",
    "Managed IT, cyber security, VoIP, data cabling, and premise security for 550+ businesses across Richmond and the Northern Neck, with a rep who actually knows your team.",
    '<a href="contact.html" class="btn btn-primary">Talk to a Rep</a><a href="peoplefirst-support.html" class="btn btn-ghost">See PeopleFirst Support</a>',
    "network",
)}

{stat_strip()}

<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="brand-rule"></div>
      <h2>Everything your business needs to run on secure, reliable technology</h2>
    </div>
    <div class="bento">
      <a class="tile b-lg tile-brand reveal" href="managed-it.html">
        <span class="icon">01</span>
        <h3>Managed IT &amp; PeopleFirst Support</h3>
        <p>Flat per-person pricing that covers every device, vendor, and cyber tool your team touches.</p>
      </a>
      <a class="tile b-md tile-accent reveal" href="cyber-security.html">
        <span class="icon">02</span>
        <h3>Cyber Security</h3>
        <p>Endpoint protection, phishing training, and 24/7 threat monitoring.</p>
      </a>
      <a class="tile b-md reveal" href="data-center.html">
        <span class="icon">03</span>
        <h3>Cloud &amp; Data Center Hosting</h3>
        <p>Private and public cloud, failover, SOC II-compliant hosting.</p>
      </a>
      <a class="tile b-sm reveal" href="voip.html">
        <span class="icon">04</span>
        <h3>Voice / VoIP</h3>
        <p>Cloud and premise voice, SIP trunking, call center.</p>
      </a>
      <a class="tile b-sm tile-accent reveal" href="data-cabling.html">
        <span class="icon">05</span>
        <h3>Data Cabling</h3>
        <p>DCJS-licensed structured cabling and infrastructure.</p>
      </a>
      <a class="tile b-sm reveal" href="premise-security.html">
        <span class="icon">06</span>
        <h3>Premise Security</h3>
        <p>Access control and camera systems, monitored.</p>
      </a>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="split reveal">
      <div>
        <span class="label">Flagship offer</span>
        <h2>PeopleFirst Support: IT priced around your people, not your devices</h2>
        <p>One flat rate per team member covers hardware, software, third-party vendor support, and cyber security, on-site and remote. No surprise device bills, no gaps in coverage.</p>
        <a href="peoplefirst-support.html" class="btn btn-ghost">How PeopleFirst works</a>
      </div>
      <div class="split-media">
        {material_panel("people", 90)}
      </div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="section-head">
      <div class="brand-rule"></div>
      <h2>Built for the way your industry actually works</h2>
    </div>
    <div class="pill-row">
      <a class="pill" href="industries.html">Healthcare</a>
      <a class="pill" href="industries.html">Legal</a>
      <a class="pill" href="industries.html">Financial Services</a>
      <a class="pill" href="industries.html">Dental</a>
      <a class="pill" href="industries.html">Automotive</a>
      <a class="pill" href="industries.html">Government</a>
      <a class="pill" href="industries.html">Hospitality</a>
      <a class="pill" href="industries.html">Retail</a>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="cta-panel reveal">
      <h2>Let's talk about your team's technology.</h2>
      <p>Tell us what you need and a rep will follow up within 1 business hour.</p>
      <div class="hero-ctas">
        <a href="contact.html" class="btn btn-primary">Talk to a Rep</a>
        <a href="tel:{PHONE_TEL}" class="btn btn-ghost-invert">Call {PHONE}</a>
      </div>
    </div>
  </div>
</section>
</main>
""" + footer()
write("index.html", home)

# ---------------------------------------------------------------------------
# MANAGED IT (pillar/service page template example)
# ---------------------------------------------------------------------------
managed_it = head(
    "Managed IT Services in Richmond, VA | CodeBlue Technology",
    "Flat-rate managed IT support for Central Virginia businesses. Hardware, software, vendor and cyber security support in one plan."
) + header("managed-it.html") + f"""
<main id="main">
{hero(
    "Managed IT Services",
    "IT support that actually knows your business.",
    "Flat-rate managed IT for growing teams. Proactive monitoring, a real help desk, and a plan built around how your people actually work.",
    '<a href="contact.html" class="btn btn-primary">Talk to a Rep</a><a href="peoplefirst-support.html" class="btn btn-ghost">Compare with PeopleFirst</a>',
    "building",
)}

{stat_strip()}

<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="brand-rule"></div>
      <h2>Three support paths, one dependable partner</h2>
    </div>
    <div class="bento">
      <div class="tile b-md reveal">
        <span class="icon">01</span><h3>Provided Software</h3>
        <p>End-point protection, data backup, cyber security, Microsoft 365 protection, and both Windows and third-party patch management, kept organized and compliant.</p>
      </div>
      <div class="tile b-md tile-accent reveal">
        <span class="icon">02</span><h3>Co-Managed IT Support</h3>
        <p>Project management, asset management, renewals management, help desk support, technology sales, and on/off-boarding management, backing up your existing IT team.</p>
      </div>
      <div class="tile b-md tile-brand reveal">
        <span class="icon">03</span><h3>PeopleFirst IT Support</h3>
        <p>Vendor management, provided equipment, licensing management, vCIO/CISO services, risk assessments, and on-site/remote support, all covered per person.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="section-head">
      <div class="brand-rule"></div>
      <h2>How does IT onboarding work?</h2>
    </div>
    <div class="steps reveal">
      <div class="step"><div class="num"></div><div><h3>Discovery and Alignment</h3><p>A discovery call or site visit to understand your needs, producing options that start your team here at CodeBlue.</p></div></div>
      <div class="step"><div class="num"></div><div><h3>Tailored Service Options</h3><p>Your business is unique, so CodeBlue forms options around your budget, goals, and requirements to ensure a great fit.</p></div></div>
      <div class="step"><div class="num"></div><div><h3>Onboarding and Integration</h3><p>Our team works to align with yours at every stage, from systems management to support metrics, aiming to exceed expectations.</p></div></div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="section-head">
      <div class="brand-rule"></div>
      <h2>Managed benefits</h2>
    </div>
    <div class="bento" style="grid-template-columns:1fr 1fr 1fr;">
      <div class="card reveal">
        <h3>Traction Forward</h3>
        <p>As your managed IT care partner, CodeBlue identifies technical risks, addresses potential threats, and prevents costly disruptions within your technology infrastructure.</p>
      </div>
      <div class="card reveal">
        <h3>Peace of Mind</h3>
        <p>We ensure you have the best technology options, maintain their optimal performance, and manage them seamlessly throughout their entire lifecycle.</p>
      </div>
      <div class="card reveal">
        <h3>Integration</h3>
        <p>CodeBlue serves as your dedicated IT department, delivering internal support, external protection, and comprehensive business solutions.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="split reveal">
      <div>
        <h2>See how PeopleFirst reframes IT around your people</h2>
        <p>Managed IT can be priced per-device or per-person. Our PeopleFirst model covers every device a team member uses under one flat rate.</p>
        <a href="peoplefirst-support.html" class="btn btn-ghost">Explore PeopleFirst Support</a>
        <div class="pill-row" style="margin-top:22px;">
          <a class="pill" href="industries.html">Healthcare</a>
          <a class="pill" href="industries.html">Legal</a>
          <a class="pill" href="industries.html">Financial Services</a>
        </div>
      </div>
      {rep_form()}
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
{hero(
    "Flagship offer",
    "Support that follows your team, not your equipment.",
    "One flat rate per person, not per device. PeopleFirst Support covers everything a team member touches: hardware, software, vendors, and cyber security, on-site and remote.",
    '<a href="contact.html" class="btn btn-primary">Talk to a Rep</a><a href="#pricing" class="btn btn-ghost">How pricing works</a>',
    "people",
)}

{stat_strip()}

<section class="section" id="pricing">
  <div class="container">
    <div class="section-head">
      <div class="brand-rule"></div>
      <h2>Plain-language pricing, no per-device math</h2>
    </div>
    <p>Most IT plans price per device. The more laptops, phones, and servers your team uses, the higher the bill, no matter how it's used. PeopleFirst flips that: every enrolled team member gets one flat monthly rate that covers every device and tool they touch. Enroll your whole staff and the math gets simpler, not more expensive.</p>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="section-head">
      <div class="brand-rule"></div>
      <h2>Six things, covered for every person</h2>
    </div>
    <div class="bento">
      <div class="tile b-md tile-brand reveal"><span class="icon">01</span><h3>Vendor Management</h3><p>We're the ones on hold with your vendors, not you.</p></div>
      <div class="tile b-md reveal"><span class="icon">02</span><h3>Provided Equipment</h3><p>Hardware sourced, provisioned, and supported as part of the plan.</p></div>
      <div class="tile b-md tile-accent reveal"><span class="icon">03</span><h3>Licensing Management</h3><p>Software licensing kept organized, current, and compliant.</p></div>
      <div class="tile b-md reveal"><span class="icon">04</span><h3>vCIO / CISO Services</h3><p>Strategic technology and security guidance at the leadership level.</p></div>
      <div class="tile b-md reveal"><span class="icon">05</span><h3>Risk Assessments</h3><p>Regular assessments that catch exposure before it becomes an incident.</p></div>
      <div class="tile b-md tile-accent reveal"><span class="icon">06</span><h3>On-Site / Remote Support</h3><p>Help wherever your team is working, in the office or out.</p></div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="split reveal">
      <div class="split-media">
        {material_panel("people", 91)}
      </div>
      <div>
        <span class="label">Behind the tech</span>
        <h2>A Client Advocate who actually knows your team</h2>
        <p>Every PeopleFirst account gets a dedicated Client Advocate, a real point of contact who knows your environment, tracks recurring issues, and escalates on your behalf instead of routing you through a ticket queue.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="section-head center">
      <div class="brand-rule"></div>
      <h2>People-based vs. device or license-based support</h2>
    </div>
    <div class="bento" style="grid-template-columns:1fr 1fr;">
      <div class="card reveal">
        <h3>Device / License-Based (old model)</h3>
        <ul>
          <li>Price grows with every device added</li>
          <li>Coverage gaps between devices and licenses</li>
          <li>Vendor issues are your problem to chase</li>
        </ul>
      </div>
      <div class="card reveal" style="border-color:var(--brand-green); box-shadow:0 18px 36px rgba(122,154,1,0.16);">
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

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="split reveal">
      <div class="card">
        <h3>PeopleFirst Support Guide</h3>
        <p>Download the full breakdown of what's included, how enrollment works, and real client examples.</p>
        <a href="resources.html" class="btn btn-ghost">Get the PDF</a>
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
{hero(
    "About us",
    "20+ years of keeping Central Virginia businesses running.",
    "Founded in 2003 and based in Richmond, VA, CodeBlue Technology has grown alongside the businesses we serve, now supporting 550+ active clients across Richmond and the Northern Neck.",
    "",
    "building",
)}

{stat_strip()}

<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="brand-rule"></div>
      <h2>Started local, stayed local</h2>
    </div>
    <p>CodeBlue Technology was founded on January 1, 2003 by Trey Hayden to service the computing and information technology needs of businesses throughout Central Virginia. Trey built a successful career in the specialty since 1990, and CodeBlue opened its doors in 2003 with a list of loyal clients that extends to over 550 active clients today.</p>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="split reveal">
      <div class="split-media">
        {material_panel("people", 94)}
      </div>
      <div>
        <span class="label">Founder & CEO</span>
        <h2>Trey Hayden</h2>
        <p>Trey was raised in Mechanicsville, Virginia and attended Hanover County Public Schools before being accepted to the School of Business at Virginia Commonwealth University to pursue his dream of being an entrepreneur and business owner. He has provided leadership, time, and resources to his staff of administrators and engineers since CodeBlue's founding in 2003, and shares his love of helping businesses through technology with nearly 30 staff members and managers today.</p>
        <div class="pill-row" style="margin-top:18px;">
          <span class="pill">VCU Alumni Owned Business</span>
          <span class="pill">Virginia Council of CEOs</span>
          <span class="pill">Mechanicsville Rotary Club</span>
          <span class="pill">West Richmond Businessmen's Association</span>
          <span class="pill">Mechanicsville Ruritan Club</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="bento" style="grid-template-columns:1fr 1fr;">
      <div class="card reveal">
        <h3>Richmond Office</h3>
        <p>9204 Center Oak Court STE C<br>Mechanicsville, VA 23116<br><a href="tel:+18045217660">(804) 521-7660</a></p>
      </div>
      <div class="card reveal">
        <h3>Northern Neck Office</h3>
        <p>5020 Richmond Rd STE A<br>Warsaw, VA 22572<br><a href="tel:+18044564500">(804) 456-4500</a></p>
      </div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="section-head">
      <div class="brand-rule"></div>
      <h2>CodeBlue Cares, our non-profit community foundation</h2>
    </div>
    <div class="bento">
      <div class="tile b-md tile-brand reveal"><span class="icon">01</span><h3>Coats for Kids</h3><p>311 coats donated to Puritan Cleaners for distribution to Central Virginia families in need.</p></div>
      <div class="tile b-md reveal"><span class="icon">02</span><h3>USO Ramen Drive</h3><p>12,024 packages of ramen donated to the USO, distributed to USO divisions throughout Virginia.</p></div>
      <div class="tile b-md tile-accent reveal"><span class="icon">03</span><h3>Little League Sponsorships</h3><p>CodeBlue sponsors area Little League organizations across Central Virginia.</p></div>
      <div class="tile b-md reveal"><span class="icon">04</span><h3>International Rotary</h3><p>CodeBlue is home to several active Rotarians in both Mechanicsville and Warsaw, VA.</p></div>
    </div>
    <p style="margin-top:20px;"><a href="https://codebluecares.org" class="btn btn-ghost">Visit CodeBlue Cares</a></p>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="cta-panel reveal">
      <h2>Let's talk about your team's technology.</h2>
      <p>Talk to a rep about what your business needs.</p>
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
      <div class="brand-rule"></div>
      <h1>Let's talk about your team's technology.</h1>
      <p style="margin-left:auto; margin-right:auto;">Call, text, or send a quick message. A CodeBlue rep will respond within 1 business hour.</p>
    </div>
    <div class="split" style="max-width:900px; margin:0 auto; align-items:start;">
      {rep_form()}
      <div class="card">
        <h3>Prefer to reach us directly?</h3>
        <p><strong>Richmond:</strong> <a href="tel:+18045217660">(804) 521-7660</a><br>
        <strong>Warsaw:</strong> <a href="tel:+18044564500">(804) 456-4500</a><br>
        <strong>Email:</strong> <a href="mailto:hello@codebluetechnology.com">hello@codebluetechnology.com</a><br>
        <strong>Service requests:</strong> <a href="mailto:service@codebluetechnology.com">service@codebluetechnology.com</a></p>
        <p id="full-form" style="margin-top:20px;">Want to pre-qualify yourself with more detail before a rep calls? The full intake form is available as a secondary option. Ask your rep for the link, or we'll add a dedicated long-form page here.</p>
      </div>
    </div>
  </div>
</section>
</main>
""" + footer()
write("contact.html", contact)

# ---------------------------------------------------------------------------
# CYBER SECURITY
# ---------------------------------------------------------------------------
cyber_security = head(
    "Cyber Security Services in Richmond, VA | CodeBlue Technology",
    "Endpoint protection, cloud security, phishing training, and dark web monitoring for Central Virginia businesses."
) + header("cyber-security.html") + f"""
<main id="main">
{hero(
    "Cyber Security",
    "Comprehensive protection, built around your business.",
    "CodeBlue Technology delivers layered cyber security services that protect your endpoints, your cloud accounts, and your people, so a single mistake doesn't become a breach.",
    '<a href="contact.html" class="btn btn-primary">Talk to a Rep</a><a href="#risk-assessment" class="btn btn-ghost">Get a free risk assessment</a>',
    "shield",
)}

{stat_strip()}

<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="brand-rule"></div>
      <h2>Three layers of protection, covered in every plan</h2>
    </div>
    <div class="bento">
      <div class="tile b-md tile-brand reveal"><span class="icon">01</span><h3>Asset Security</h3><p>Endpoint detection and response, ransomware protection with roll-back, off-site backup replication, and drive encryption on every device.</p></div>
      <div class="tile b-md reveal"><span class="icon">02</span><h3>Cloud Security</h3><p>Microsoft 365 and Google Workspace data security, multi-factor authentication, and cloud-to-cloud backup and replication.</p></div>
      <div class="tile b-md tile-accent reveal"><span class="icon">03</span><h3>End User Training</h3><p>Monthly phishing simulations, cyber security best-practice updates, and documented policy and procedure for your organization.</p></div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="section-head">
      <div class="brand-rule"></div>
      <h2>Security first, in three steps</h2>
    </div>
    <div class="steps reveal">
      <div class="step"><div class="num"></div><div><h3>Discovery</h3><p>Network-wide asset and access discovery establishes your baseline exposure and produces an actionable remediation plan.</p></div></div>
      <div class="step"><div class="num"></div><div><h3>Scaling Securely</h3><p>Risks and vulnerabilities are captured in a Written Information Security Plan, reviewed quarterly as new technology emerges.</p></div></div>
      <div class="step"><div class="num"></div><div><h3>Risk Remediation</h3><p>We monitor the dark web for compromised email addresses and passwords tied to your business and act on them right away.</p></div></div>
    </div>
  </div>
</section>

<section class="section" id="risk-assessment" style="padding-top:0;">
  <div class="container">
    <div class="split reveal">
      <div class="card">
        <span class="label">Free Risk Assessment</span>
        <h3>Understand your network from a security standpoint</h3>
        <p>Every assessment renders a free report with clear remediation steps to take, no obligation.</p>
        <a href="contact.html" class="btn btn-ghost">Schedule your assessment</a>
      </div>
      {rep_form()}
    </div>
  </div>
</section>
</main>
""" + footer()
write("cyber-security.html", cyber_security)

# ---------------------------------------------------------------------------
# DATA CENTER / CLOUD HOSTING
# ---------------------------------------------------------------------------
data_center = head(
    "Cloud & Data Center Hosting in Richmond, VA | CodeBlue Technology",
    "Private and public cloud hosting, hardware hosting, and SOC II compliant disaster recovery from Richmond's largest private data center."
) + header("data-center.html") + f"""
<main id="main">
{hero(
    "Cloud & Data Center Hosting",
    "Richmond's largest private cloud.",
    "CodeBlue Technology hosts dedicated, compliant, highly resilient server environments, matched to your workload and backed by a local team you can actually call.",
    '<a href="contact.html" class="btn btn-primary">Talk to a Rep</a><a href="data-cabling.html" class="btn btn-ghost">See data cabling</a>',
    "building",
)}

{stat_strip()}

<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="brand-rule"></div>
      <h2>Hosting built around your workload</h2>
    </div>
    <div class="bento">
      <div class="tile b-md tile-brand reveal"><span class="icon">01</span><h3>Hosted Virtual Servers</h3><p>Dedicated Windows Server environments with maintenance, OS updates, and backup and recovery included.</p></div>
      <div class="tile b-md reveal"><span class="icon">02</span><h3>Hardware Hosting</h3><p>Rack, half-rack, or full-rack hosting with power redundancy and geographic diversity for failover.</p></div>
      <div class="tile b-md tile-accent reveal"><span class="icon">03</span><h3>Disaster Recovery</h3><p>RTO and RPO designed around your workflow, on-net with Comcast, Verizon, Level 3, Segra and more.</p></div>
      <div class="tile b-md reveal"><span class="icon">04</span><h3>Privacy &amp; Compliance</h3><p>SOC II compliant data centers and cloud offerings, audited against the highest security standards.</p></div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="section-head">
      <div class="brand-rule"></div>
      <h2>How does CodeBlue Cloud work?</h2>
    </div>
    <div class="steps reveal">
      <div class="step"><div class="num"></div><div><h3>Discovery and Alignment</h3><p>A discovery call or site visit to understand your needs, producing real options for your business.</p></div></div>
      <div class="step"><div class="num"></div><div><h3>Tailored Service Options</h3><p>We shape resources and support around your budget, goals, and requirements.</p></div></div>
      <div class="step"><div class="num"></div><div><h3>Onboarding and Integration</h3><p>Our team aligns with yours at every stage, from systems management to support metrics.</p></div></div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="split reveal">
      <div>
        <span class="label">Private Cloud Hosting</span>
        <h2>Stability and control that public cloud can't match</h2>
        <p>Private cloud hosting with CodeBlue avoids the unexpected price changes and program cancellations that come with public cloud services, so your costs and access stay consistent.</p>
        <a href="contact.html" class="btn btn-ghost">Talk to a rep</a>
      </div>
      <div class="split-media">
        {material_panel("building", 92)}
      </div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="cta-panel reveal">
      <h2>Let's talk about your team's technology.</h2>
      <p>Tell us what you need and a rep will follow up within 1 business hour.</p>
      <div class="hero-ctas">
        <a href="contact.html" class="btn btn-primary">Talk to a Rep</a>
        <a href="tel:{PHONE_TEL}" class="btn btn-ghost-invert">Call {PHONE}</a>
      </div>
    </div>
  </div>
</section>
</main>
""" + footer()
write("data-center.html", data_center)

# ---------------------------------------------------------------------------
# VOICE / VOIP
# ---------------------------------------------------------------------------
voip = head(
    "Voice / VoIP Services in Richmond, VA | CodeBlue Technology",
    "Cloud and premise voice systems, SIP trunking, call center and conference room solutions, HIPAA compliant and built to scale."
) + header("voip.html") + f"""
<main id="main">
{hero(
    "Voice / VoIP",
    "Your office phone just got a lot more capable.",
    "CodeBlue's voice platform has empowered businesses since 2003, on-premise, in the cloud, or both, with the features your team actually uses every day.",
    '<a href="contact.html" class="btn btn-primary">Talk to a Rep</a><a href="#demo" class="btn btn-ghost">Request a demo</a>',
    "network",
)}

{stat_strip()}

<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="brand-rule"></div>
      <h2>Essential features from a leading platform</h2>
    </div>
    <div class="bento">
      <div class="tile b-md tile-brand reveal"><span class="icon">01</span><h3>Find / Follow Me</h3><p>Calls route to your desk and other specified locations, so you're reachable wherever you're working.</p></div>
      <div class="tile b-md reveal"><span class="icon">02</span><h3>Visual Voicemail</h3><p>Scan voicemails for key information and search transcripts for names, addresses, and numbers.</p></div>
      <div class="tile b-md tile-accent reveal"><span class="icon">03</span><h3>Chat and Text</h3><p>Secure internal chat plus image and audio texting, directly through your business phone number.</p></div>
      <div class="tile b-md reveal"><span class="icon">04</span><h3>HIPAA Compliant Voice</h3><p>Redundant, encrypted endpoints built to meet healthcare regulatory requirements.</p></div>
    </div>
  </div>
</section>

<section class="section" id="demo" style="padding-top:0;">
  <div class="container">
    <div class="split reveal">
      <div>
        <span class="label">Moving to VoIP</span>
        <h2>Keep your numbers and your calls, without interruption</h2>
        <p>Businesses starting on-premise can migrate to the cloud without rebuilding their system, or run both in tandem with seamless hand-off between environments. Our voice engineers train your team on every feature, hands-on.</p>
        <div class="pill-row" style="margin-top:22px;">
          <span class="pill">Hardware Phone Systems</span>
          <span class="pill">Cloud Hosted Voice</span>
          <span class="pill">Conference Room Systems</span>
          <span class="pill">SIP Voice Services</span>
          <span class="pill">Call Center Solutions</span>
        </div>
      </div>
      {rep_form()}
    </div>
  </div>
</section>
</main>
""" + footer()
write("voip.html", voip)

# ---------------------------------------------------------------------------
# DATA CABLING
# ---------------------------------------------------------------------------
data_cabling = head(
    "Data Cabling Services in Richmond, VA | CodeBlue Technology",
    "DCJS-licensed low voltage contracting: structured cabling, data closet build-outs, and cabling supplies for Central Virginia businesses."
) + header("data-cabling.html") + f"""
<main id="main">
{hero(
    "Data Cabling",
    "From the wall to the desk.",
    "Properly scoped, installed, and documented wiring is part of the construction of your space. CodeBlue plans, installs, and documents it so your business connects without the hassle.",
    '<a href="contact.html" class="btn btn-primary">Talk to a Rep</a><a href="premise-security.html" class="btn btn-ghost">See premise security</a>',
    "network",
)}

{stat_strip()}

<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="brand-rule"></div>
      <h2>How cabling contracting works</h2>
    </div>
    <div class="steps reveal">
      <div class="step"><div class="num"></div><div><h3>Discovery and Alignment</h3><p>We review technical drawings from your contractor or designer and plan data locations for computers, access points, printers, and smart devices.</p></div></div>
      <div class="step"><div class="num"></div><div><h3>Tailored Cabling Plan</h3><p>We recommend optimal central and termination points, maximizing function while minimizing cost.</p></div></div>
      <div class="step"><div class="num"></div><div><h3>Scheduling and Installation</h3><p>Turnkey proposals cover all materials, labor, and documentation, coordinated closely with your general contractor's schedule.</p></div></div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="section-head">
      <div class="brand-rule"></div>
      <h2>Beyond the cable run</h2>
    </div>
    <div class="bento">
      <div class="tile b-md tile-brand reveal"><span class="icon">01</span><h3>Professional Planning</h3><p>Layout, cable paths, cable management, and code adherence, working independently or alongside your general contractor.</p></div>
      <div class="tile b-md reveal"><span class="icon">02</span><h3>Data Room Build-Out</h3><p>Rack storage, HIPAA-compliant access tracking, temperature monitoring, camera security, and backup power for your data closet.</p></div>
      <div class="tile b-md tile-accent reveal"><span class="icon">03</span><h3>Supplies &amp; Materials</h3><p>Authorized supplier for racks, cabinets, patch paneling, fiber optic accessories, and outdoor and underground cabling.</p></div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="split reveal">
      <div>
        <span class="label">Licensed low voltage contractor</span>
        <h2>Virginia code-compliant, coordinated with your build</h2>
        <p>We coordinate conduit and box installation before drywall and paint, in-ground conduit ahead of slab and concrete, and D-rings and cable tie-offs before ceiling and grid work, creating real cost savings for you and your contractor. CodeBlue also offers preferred pricing for local commercial contractors across Virginia.</p>
        <a href="contact.html" class="btn btn-ghost">Get a pricing quote</a>
      </div>
      {rep_form()}
    </div>
  </div>
</section>
</main>
""" + footer()
write("data-cabling.html", data_cabling)

# ---------------------------------------------------------------------------
# PREMISE SECURITY & CAMERAS
# ---------------------------------------------------------------------------
premise_security = head(
    "Premise Security & Cameras in Richmond, VA | CodeBlue Technology",
    "DCJS-licensed access control and IP security camera systems for Central Virginia businesses."
) + header("premise-security.html") + f"""
<main id="main">
{hero(
    "Premise Security & Cameras",
    "Protect your space, inside and out.",
    "CodeBlue Technology designs access control and networked camera systems around your entrances, your risk, and your growth, installed by licensed DCJS technicians.",
    '<a href="contact.html" class="btn btn-primary">Talk to a Rep</a><a href="data-cabling.html" class="btn btn-ghost">See data cabling</a>',
    "shield",
)}

{stat_strip()}

<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="brand-rule"></div>
      <h2>Three solution areas, one integrated system</h2>
    </div>
    <div class="bento">
      <div class="tile b-md tile-brand reveal"><span class="icon">01</span><h3>Outdoor Camera Solutions</h3><p>From static parking lot cameras to mobile units with color low-light imaging and face and license plate detection.</p></div>
      <div class="tile b-md reveal"><span class="icon">02</span><h3>Indoor Camera Solutions</h3><p>Professionally sourced and installed by licensed DCJS technicians, matched to the area they protect and discreetly integrated.</p></div>
      <div class="tile b-md tile-accent reveal"><span class="icon">03</span><h3>Smart Access Control</h3><p>Custom-designed around your entrances and exits, with seamless integration between access control and cameras.</p></div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="split reveal">
      <div>
        <span class="label">Managed Security</span>
        <h2>Access changes handled for you, not by you</h2>
        <p>Updating door access, issuing new keys, handling replacement cards, and preventing false alarms adds up fast. Our partner support program turns that complexity into a hassle-free service, so you can focus on running your business.</p>
        <a href="contact.html" class="btn btn-ghost">Talk to a rep</a>
      </div>
      <div class="split-media">
        {material_panel("shield", 93)}
      </div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="card reveal" style="max-width:640px;">
      <h3>Department of Criminal Justice Services licensed</h3>
      <p>Hiring a DCJS-certified contractor ensures your security installation meets Virginia's regulated standards for safety, reliability, and compliance. CodeBlue Technology's DCJS ID is 11-16835.</p>
    </div>
  </div>
</section>
</main>
""" + footer()
write("premise-security.html", premise_security)

# ---------------------------------------------------------------------------
# INDUSTRIES
# ---------------------------------------------------------------------------
industries_data = [
    ("Financial Services", "Technology Support for Financial Institutions",
     "The financial services industry needs both operational efficiency and strict regulatory compliance. CodeBlue Technology delivers robust, secure, scalable IT so financial firms operate without disruption while meeting the standards regulators require.",
     ["Data security and encryption for sensitive financial data", "Regulatory compliance management for SOX, GLBA, and PCI DSS", "24/7 monitoring and support", "Disaster recovery and business continuity planning"]),
    ("Automotive &amp; Collision Repair", "IT Built for the Shop Floor",
     "Automotive and collision repair shops depend on digital diagnostics, customer communication, and daily operations staying online. CodeBlue keeps telephony, imaging, wireless, and digital signage running so your team can focus on the work in front of them.",
     ["Telephony solutions for reliable customer and supplier communication", "Imaging and diagnostics support for accurate workflow management", "Wireless network stability across the shop floor", "Digital signage management for customer engagement"]),
    ("Healthcare", "Healthcare and Medical Workers Depend on IT",
     "Hospitals and healthcare practices need IT that supports patient care, urgent response, and secure operations. CodeBlue optimizes systems for emergency coordination, secures patient data and facility access, and monitors sensitive areas with high-quality cameras.",
     ["Telephony and communication systems for staff, patients, and emergency services", "Access control and data security for patient information", "Priority urgent response support", "Security cameras and monitoring"]),
    ("Legal", "Legal Practice IT for Secure, Organized Operations",
     "Law firms manage sensitive client data, case management software, and secure communication every day. CodeBlue protects confidential information, supports the software you already use, and manages server and cloud storage for critical documents.",
     ["Secure data management and encryption for client files", "Case management software support", "Telephony and communication support for clients, courts, and colleagues", "Server and cloud storage for case histories"]),
    ("Dental", "Dental Technology Support for Secure Patient Care",
     "Dental practices depend on patient charting software, HIPAA-compliant records, and reliable phone systems running without interruption. CodeBlue supports the premise servers and dental-specific software your practice runs on.",
     ["Patient charting software support", "Secure, HIPAA-compliant email and data storage", "Telephony and communication support", "Premise server and dental software maintenance"]),
    ("Government", "State and Local Government Co-Managed IT",
     "State and local governments manage complex systems, protect sensitive data, and communicate with citizens every day. CodeBlue supports citizen software systems, secure email and data storage, and technology procurement that fits public-sector budgets.",
     ["Citizen software management", "Secure, compliant email and data storage", "Telephony and communication support", "Technology purchasing and procurement"]),
]
industry_cards = "\n".join(f"""    <div class="card reveal" style="margin-bottom:20px;">
      <span class="label">{name}</span>
      <h3>{headline}</h3>
      <p>{body}</p>
      <ul>
        {"".join(f"<li>{b}</li>" for b in bullets)}
      </ul>
    </div>""" for name, headline, body, bullets in industries_data)

industries = head(
    "Industries We Serve | CodeBlue Technology",
    "CodeBlue Technology serves financial services, automotive, healthcare, legal, dental, and government organizations across Central Virginia."
) + header("industries.html") + f"""
<main id="main">
{hero(
    "Industries",
    "Built for the way your industry actually works.",
    "Every industry has different rules, risk, and daily workflow. Here's how CodeBlue Technology tailors IT support to the businesses we serve most.",
    '<a href="contact.html" class="btn btn-primary">Talk to a Rep</a>',
    "people",
)}
{stat_strip()}
<section class="section">
  <div class="container">
{industry_cards}
  </div>
</section>
<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="cta-panel reveal">
      <h2>Don't see your industry?</h2>
      <p>We support businesses across Central Virginia beyond the industries above. Tell us what you do and we'll show you how CodeBlue fits.</p>
      <div class="hero-ctas">
        <a href="contact.html" class="btn btn-primary">Talk to a Rep</a>
      </div>
    </div>
  </div>
</section>
</main>
""" + footer()
write("industries.html", industries)

# ---------------------------------------------------------------------------
# RESOURCES
# ---------------------------------------------------------------------------
resources = head(
    "Resources | CodeBlue Technology",
    "Guides, checklists, and downloads from CodeBlue Technology, plus the CodeBlueTech podcast."
) + header("resources.html") + f"""
<main id="main">
{hero(
    "Resources",
    "Guides and tools for business owners.",
    "Free downloads, checklists, and a free network risk assessment, no obligation.",
    '<a href="contact.html" class="btn btn-primary">Talk to a Rep</a>',
    "building",
)}
{stat_strip()}
<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="brand-rule"></div>
      <h2>Free downloads</h2>
    </div>
    <div class="bento">
      <div class="tile b-md tile-brand reveal">
        <span class="icon">PDF</span>
        <h3>25 Signs Your Business Is Ready for Managed IT</h3>
        <p>A practical checklist for business owners weighing outsourced IT.</p>
        <a href="https://www.codebluetechnology.com/wp-content/uploads/2026/05/CodeBlue-Technology-25-Signs-Your-Business-Needs-Outsourced-IT.pdf" class="btn btn-ghost" style="margin-top:12px;">Download the PDF</a>
      </div>
      <div class="tile b-md reveal">
        <span class="icon">PPT</span>
        <h3>CodeBlue Partnership Benefits</h3>
        <p>A short presentation for owners on what a CodeBlue partnership includes.</p>
        <a href="https://www.codebluetechnology.com/wp-content/uploads/2024/10/CodeBlue-Partnership-Benefits.pptx" class="btn btn-ghost" style="margin-top:12px;">Download the presentation</a>
      </div>
      <div class="tile b-md tile-accent reveal">
        <span class="icon">SEC</span>
        <h3>Cyber Security Checklist</h3>
        <p>Three things every small or mid-sized business needs to get right, from our cyber security team.</p>
        <a href="cyber-security.html" class="btn btn-ghost" style="margin-top:12px;">See cyber security</a>
      </div>
      <div class="tile b-md reveal">
        <span class="icon">MIC</span>
        <h3>CodeBlueTech Podcast</h3>
        <p>Conversations on technology and business, from the CodeBlue Technology team.</p>
        <a href="https://itunes.apple.com/us/podcast/codebluetech/id1312995332?mt=2" class="btn btn-ghost" style="margin-top:12px;">Listen on Apple Podcasts</a>
      </div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="split reveal">
      <div class="card">
        <span class="label">Free Risk Assessment</span>
        <h3>Understand your network from a security standpoint</h3>
        <p>Every assessment renders a free report with remediation steps to take, no strings attached.</p>
        <a href="contact.html" class="btn btn-ghost">Schedule your assessment</a>
      </div>
      <div class="card">
        <span class="label">CodeBlue Cares</span>
        <h3>Our non-profit community foundation</h3>
        <p>From Coats for Kids to the USO Ramen Drive, CodeBlue gives back to the Central Virginia community we serve.</p>
        <a href="https://codebluecares.org" class="btn btn-ghost">Visit CodeBlue Cares</a>
      </div>
    </div>
  </div>
</section>
</main>
""" + footer()
write("resources.html", resources)

# ---------------------------------------------------------------------------
# CAREERS
# ---------------------------------------------------------------------------
careers = head(
    "Careers at CodeBlue Technology | Richmond, VA",
    "Join the CodeBlue Technology team in Richmond, VA. Current openings in client relations and IT solutions consulting."
) + header("careers.html") + f"""
<main id="main">
{hero(
    "Careers",
    "Let's grow together.",
    "CodeBlue is building a culture where our team can do their best work: IT support, technology consultation, and customer experience, done well.",
    '<a href="#openings" class="btn btn-primary">See open positions</a><a href="contact.html" class="btn btn-ghost">Ask us a question</a>',
    "people",
)}
{stat_strip()}
<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="brand-rule"></div>
      <h2>What is CodeBlue Technology?</h2>
    </div>
    <p>CodeBlue Technology is a trusted leader in IT management and support, delivering tailored technology solutions to small and mid-sized businesses: managed IT, cyber security, cloud, and network infrastructure. We serve healthcare, legal, manufacturing, and professional services clients, and we build long-term partnerships through real service and real solutions. Joining the CodeBlue team means becoming part of a mission-driven group solving real problems for businesses that depend on us.</p>
  </div>
</section>

<section class="section" id="openings" style="padding-top:0;">
  <div class="container">
    <div class="section-head">
      <div class="brand-rule"></div>
      <h2>Open positions</h2>
    </div>
    <div class="bento" style="grid-template-columns:1fr 1fr;">
      <div class="card reveal">
        <h3>Client Relationship Coordinator</h3>
        <p class="sub">Richmond, VA (On-site)</p>
        <p>You're a customer advocate, driven to bring value to every relationship. As part of an integrated sales team, you'll set schedules and set the pace for CodeBlue's sales reps while bringing awareness to new offerings and services.</p>
        <a href="https://www.codebluetechnology.com/careers/" class="btn btn-ghost">View full description</a>
      </div>
      <div class="card reveal">
        <h3>IT Solutions Consultant</h3>
        <p class="sub">Richmond, VA (On-site)</p>
        <p>You're a technical sales hunter who brings IT experience into new solutions for small and mid-sized businesses. As a Solutions Consultant, you'll join a team of engineers and client coordinators to plan and grow business in your territory.</p>
        <a href="https://www.codebluetechnology.com/careers/" class="btn btn-ghost">View full description</a>
      </div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="cta-panel reveal">
      <h2>Don't see the right role?</h2>
      <p>We're always glad to hear from people who care about doing good work. Reach out and tell us what you're looking for.</p>
      <div class="hero-ctas">
        <a href="contact.html" class="btn btn-primary">Get in touch</a>
      </div>
    </div>
  </div>
</section>
</main>
""" + footer()
write("careers.html", careers)

print("\nDone.")
