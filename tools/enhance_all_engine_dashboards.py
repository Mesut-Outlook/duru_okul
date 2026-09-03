#!/usr/bin/env python3
"""
Enhances havo3/*/js/engine.js so that:
1. renderHome renders proeftoetsen grouped per Hoofdstuk with chapter accordions, chapter average grade, and badges.
2. renderDashboard renders the Hoofdstukken Overzicht & Cijfers table.
"""

import glob
import re

engine_files = glob.glob("/home/mesuto/Documents/PROJELER/duru_okul/havo3/*/js/engine.js")

for fp in engine_files:
    with open(fp, "r", encoding="utf-8") as f:
        code = f.read()

    vak = fp.split("/")[-3]
    icoon = "📝"
    if vak == "duits": icoon = "🇩🇪"
    elif vak == "engels": icoon = "🇬🇧"
    elif vak == "geschiedenis": icoon = "🕰️"
    elif vak == "wiskunde": icoon = "⚖️"
    elif vak == "aardrijkskunde": icoon = "🗺️"
    elif vak == "frans": icoon = "🇫🇷"
    elif vak == "nederlands": icoon = "📖"
    elif vak == "natuurkunde": icoon = "⚛️"
    elif vak == "scheikunde": icoon = "🧪"
    elif vak == "biologie": icoon = "🧬"
    elif vak == "economie": icoon = "🏛️"
    elif vak == "maatschappijleer": icoon = "🏛️"

    # Replace renderHome proeftoetsen flat grid with chapter accordions if not already
    if "chapter-accordion" not in code and "DURU.examens && DURU.examens.length" in code:
        old_pattern = r"(// Oefentoetsen-sectie[^\n]*\n\s*if\s*\(DURU\.examens\s*&&\s*DURU\.examens\.length\)\s*\{)(.*?)(html\s*\+=\s*'<div class=\"grid cols-3\">';\s*DURU\.examens\.forEach.*?html\s*\+=\s*'</div>';\s*\})"
        
        def repl_home(m):
            prefix = m.group(1)
            return prefix + f'''
      html += '<div class="sectie-titel"><h3>📝 Oefentoetsen per Hoofdstuk — test jezelf op tijd!</h3><div class="lijn"></div></div>';
      html += '<p style="margin:0 4px 14px;color:var(--grijs)">Kies hieronder een Hoofdstuk. Elk hoofdstuk bevat gerichte proeftoetsen. Klik op een hoofdstuk om deze in of uit te klappen.</p>';
      
      html += '<div class="accordion-controls">' +
        '<button class="btn ghost klein" onclick="DURU.toggleAllAccordions(true)">📂 Alles uitvouwen</button>' +
        '<button class="btn ghost klein" onclick="DURU.toggleAllAccordions(false)">📁 Alles inklappen</button>' +
        '</div>';

      var exDataHome;
      try {{ exDataHome = JSON.parse(localStorage.getItem(SLEUTEL.replace(/_v1$/, "_examens_v1"))) || {{ history: [] }}; }} catch (e) {{ exDataHome = {{ history: [] }}; }}
      exDataHome.history = exDataHome.history || [];

      var chaptersMap = {{}};
      (DURU.hoofdstukken || []).forEach(function (hf) {{
        chaptersMap[hf.nr] = {{ meta: hf, examens: [] }};
      }});

      DURU.examens.forEach(function (ex) {{
        var hfNr = ex.hoofdstuk || 1;
        if (!chaptersMap[hfNr]) {{
          chaptersMap[hfNr] = {{
            meta: {{ nr: hfNr, titel: ex.hoofdstukTitel || ("Hoofdstuk " + hfNr), icoon: ex.icoon || "{icoon}", intro: "" }},
            examens: []
          }};
        }}
        chaptersMap[hfNr].examens.push(ex);
      }});

      Object.keys(chaptersMap).sort(function(a, b) {{ return parseInt(a, 10) - parseInt(b, 10); }}).forEach(function (hfNr) {{
        var group = chaptersMap[hfNr];
        var meta = group.meta;
        var exams = group.examens;
        if (!exams.length) return;

        var totalExams = exams.length;
        var completedExams = 0;
        var sumPcts = 0;
        exams.forEach(function(ex) {{
          var atts = exDataHome.history.filter(function (a) {{ return a.examId === ex.id; }});
          if (atts.length > 0) {{
            completedExams++;
            sumPcts += (atts[0].pct || 0);
          }}
        }});
        var avgScore = completedExams > 0 ? cijferStr(sumPcts / completedExams) : null;

        html += '<details class="chapter-accordion" id="home-ch-acc-' + meta.nr + '" open>';
        html += '<summary class="chapter-header">' +
          '<div class="ch-icon">' + (meta.icoon || "{icoon}") + '</div>' +
          '<div class="ch-info">' +
            '<span class="ch-badge">Hoofdstuk ' + meta.nr + '</span>' +
            '<div class="ch-title">' + esc(meta.titel) + '</div>' +
            (meta.intro ? '<div class="ch-sub">' + esc(meta.intro) + '</div>' : '') +
          '</div>' +
          '<div class="ch-meta">' +
            '<div class="ch-stats">' +
              '<div>' + totalExams + ' toetsen · ' + (totalExams * 20) + ' vragen</div>' +
              (completedExams > 0 ? '<div style="color:var(--groen);font-size:12px;font-weight:700;">✓ ' + completedExams + '/' + totalExams + ' gemaakt (Gem. ' + avgScore + ')</div>' : '<div style="color:var(--grijs-licht);font-size:12px;">Nog niet gemaakt</div>') +
            '</div>' +
            '<div class="ch-chevron">▼</div>' +
          '</div>' +
        '</summary>';

        html += '<div class="chapter-content"><div class="grid cols-3">';
        exams.forEach(function (ex) {{
          var atts = exDataHome.history.filter(function (a) {{ return a.examId === ex.id; }});
          var statusHtml;
          if (atts.length > 0) {{
            var pcts = atts.map(function (a) {{ return a.pct || 0; }});
            var maxPct = Math.max.apply(null, pcts);
            var laatstePct = atts[0].pct || 0;
            statusHtml =
              '<div class="ex-status">' +
                '<span class="tag" style="background:var(--groen-zacht);color:var(--groen)">✓ ' + atts.length + 'x gemaakt</span>' +
                '<div style="font-size:12px;font-weight:800;margin-top:6px;color:' + (laatstePct >= 55 ? 'var(--groen)' : 'var(--oranje)') + '">⏱️ Laatste: ' + cijferStr(laatstePct) + ' (' + laatstePct + '%)</div>' +
                '<div style="font-size:12px;font-weight:800;margin-top:2px;color:var(--groen)">🏆 Beste: ' + cijferStr(maxPct) + '</div>' +
              '</div>';
          }} else {{
            statusHtml =
              '<div class="ex-status">' +
                '<span class="tag">Proeftoets</span>' +
                '<div style="font-size:12px;font-weight:700;margin-top:6px;color:var(--grijs-licht)">Nog niet gemaakt</div>' +
              '</div>';
          }}
          html += '<div class="topic-card" onclick="DURU.gaNaar(\\'examens\\',\\'' + ex.id + '\\')">' +
            '<div class="ico" style="background:var(--paars-zacht)">' + (ex.icoon || "📝") + '</div>' +
            '<h4>' + ex.titel + '</h4>' +
            '<p>' + (ex.vragen.length) + ' vragen · ⏱️ ' + (ex.duurMin || 20) + ' min</p>' +
            statusHtml + '</div>';
        }});
        html += '</div></div></details>';
      }});
    }}'''
        code = re.sub(old_pattern, repl_home, code, flags=re.DOTALL)

    # Enhance renderDashboard with Hoofdstukken Overzicht table if not already added
    if "Hoofdstukken Overzicht" not in code:
        needle = r"(html\s*\+=\s*'<div class=\"sectie-titel\"><h3>📖 Oefenen per onderwerp</h3><div class=\"lijn\"></div></div>';)"
        
        def repl_dash(m):
            matched = m.group(1)
            table_str = r'''// Hoofdstukken Overzicht & Cijfers
    html += '<div class="sectie-titel"><h3>📖 Hoofdstukken Overzicht &amp; Cijfers (Ünite Başarı Karnesi)</h3><div class="lijn"></div></div>';
    html += '<p style="margin:0 4px 14px;color:var(--grijs)">Okul sınavları ünite bazında yapıldığı için her ünitenin ortalaması ve durumu aşağıda listelenmiştir.</p>';
    html += '<table class="nask" style="margin-bottom:28px;">';
    html += '<thead><tr><th style="text-align:left;">Hoofdstuk</th><th>Oefeningen</th><th>Proeftoetsen</th><th>Gemiddeld Cijfer</th><th>Beste Cijfer</th><th>Laatste Toets</th><th>Status</th></tr></thead><tbody>';

    (DURU.hoofdstukken || []).forEach(function (h) {
      var ow = DURU.onderwerpenVan ? DURU.onderwerpenVan(h.nr) : [];
      var owDone = ow.filter(function(o) { return (P.pogingen && P.pogingen[o.id] > 0) || (P.beste && P.beste[o.id] > 0); }).length;
      
      var hfExams = (DURU.examens || []).filter(function(ex) { return (ex.hoofdstuk || 1) === h.nr; });
      var hfAttempts = (exData.history || []).filter(function(a) {
        var hfNr = a.hoofdstuk;
        if (!hfNr && a.examId) {
          var m = a.examId.match(/ex-h\d+-[a-z]+-(\d+)/i);
          if (m) hfNr = Math.floor((parseInt(m[1], 10) - 1) / 5) + 1;
        }
        return (hfNr || 1) === h.nr;
      });

      var examCount = hfAttempts.length;
      var sumPcts = 0;
      var maxPct = 0;
      var lastPct = 0;
      var lastDatum = "-";

      if (examCount > 0) {
        hfAttempts.forEach(function(a) {
          sumPcts += (a.pct || 0);
          if ((a.pct || 0) > maxPct) maxPct = a.pct;
        });
        lastPct = hfAttempts[0].pct || 0;
        lastDatum = (hfAttempts[0].datum || "-").split(" ")[0];
      }

      var avgGrade = examCount > 0 ? cijferStr(sumPcts / examCount) : "—";
      var maxGrade = examCount > 0 ? cijferStr(maxPct) : "—";
      var lastGrade = examCount > 0 ? cijferStr(lastPct) : "—";

      var avgNum = examCount > 0 ? (1 + (sumPcts / examCount) / 100 * 9) : 0;
      var statusBadge = '<span style="color:var(--grijs-licht);">⏳ Niet gestart</span>';
      if (examCount > 0) {
        if (avgNum >= 8.5) statusBadge = '<span style="color:var(--groen);font-weight:800;">🌟 Uitmuntend</span>';
        else if (avgNum >= 7.0) statusBadge = '<span style="color:var(--groen);font-weight:700;">👍 Goed</span>';
        else if (avgNum >= 5.5) statusBadge = '<span style="color:var(--blauw);font-weight:700;">✔️ Voldoende</span>';
        else statusBadge = '<span style="color:var(--oranje);font-weight:800;">⚠️ Tekrar Gerekli</span>';
      }

      html += '<tr>';
      html += '<td style="text-align:left;font-weight:700;">' + (h.icoon || "📖") + ' Hoofdstuk ' + h.nr + ': ' + esc(h.titel) + '</td>';
      html += '<td>' + owDone + '/' + ow.length + '</td>';
      html += '<td><strong>' + examCount + '</strong> / ' + hfExams.length + ' gemaakt</td>';
      html += '<td><span style="font-size:15px;font-weight:800;color:' + (avgNum >= 5.5 ? 'var(--groen)' : (examCount > 0 ? 'var(--oranje)' : 'var(--grijs-licht)')) + ';">' + avgGrade + '</span></td>';
      html += '<td><strong style="color:var(--groen);">' + maxGrade + '</strong></td>';
      html += '<td>' + lastGrade + ' <small style="color:var(--grijs);font-size:11px;">(' + esc(lastDatum) + ')</small></td>';
      html += '<td>' + statusBadge + '</td>';
      html += '</tr>';
    });
    html += '</tbody></table>';

    '''
            return table_str + matched

        code = re.sub(needle, repl_dash, code)

    with open(fp, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"Updated {fp}")
