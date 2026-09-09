"""Inline SVG illustrations, injected into stop text with {{svg:name}}.
Classes: .s ink stroke, .t iron stroke, .f iron tint fill, .w water fill,
.lb label (.i iron, .wt water). All colours come from the page's CSS variables."""

def wrap(name, vb, body, cap):
    return ('<div class="ill" data-ill="%s"><svg viewBox="%s" role="img" aria-label="%s">%s</svg>'
            '<div class="cap">%s</div></div>') % (name, vb, cap.replace('"','&quot;'), body, cap)

SVG = {}

# 1. Why the Heath drains the way it does
SVG['geology'] = wrap('geology', '0 0 320 175', '''
<defs><pattern id="hatch" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="7" stroke="currentColor" stroke-width=".7" opacity=".35"/></pattern></defs>
<path fill="url(#hatch)" d="M0 116 L320 124 L320 170 L0 170 Z"/>
<path class="f" d="M0 62 C60 42 100 42 140 52 C190 64 214 90 236 98 L0 92 Z"/>
<path class="s" d="M0 92 L320 100" stroke-dasharray="3 3"/>
<path class="s" d="M0 116 L320 124"/>
<path class="s" d="M0 62 C60 42 100 42 140 52 C190 64 220 122 262 127 C292 130 310 122 320 120"/>
<path class="t" d="M78 22 L78 40 M72 34 L78 41 L84 34" /><path class="t" d="M118 22 L118 40 M112 34 L118 41 L124 34"/><path class="t" d="M158 26 L158 44 M152 38 L158 45 L164 38"/>
<path class="t" stroke-dasharray="2.5 2.5" d="M80 50 L84 88 L236 96 M120 50 L122 90 M160 56 L162 92"/>
<path class="t" d="M236 96 L248 104 M243 105 L249 105 L248 99"/>
<ellipse class="w" cx="266" cy="126" rx="26" ry="5"/>
<rect class="w" x="196" y="74" width="20" height="18"/>
<path class="s" d="M192 68 L196 68 L196 92 L216 92 L216 68 L220 68"/>
<path class="s" d="M198 66 L214 66 L206 58 Z"/>
<text class="lb" x="8" y="84">Bagshot Sands</text>
<text class="lb" x="8" y="110">Claygate Beds</text>
<text class="lb" x="8" y="146">London Clay</text>
<text class="lb i" x="66" y="16">rain</text>
<text class="lb i" x="234" y="90">spring</text>
<text class="lb wt" x="248" y="144">pond</text>
<text class="lb i" x="224" y="66">the villa</text>
''', 'Rain sinks through the sand, meets the clay, and leaves sideways. Every pond, every sand pit and every flooded cellar on the Heath follows from that.')

# 2. The Sham Bridge, from the terrace and from the side
SVG['sham-bridge'] = wrap('sham-bridge', '0 0 320 172', '''
<text class="lb" x="8" y="14">From the terrace</text>
<path class="w" d="M20 86 C50 82 70 92 100 88 C130 84 160 92 190 88 C220 84 250 92 300 88 L300 100 L20 100 Z"/>
<path class="f" d="M44 36 L276 36 L276 82 L246 82 L246 62 A18 18 0 0 0 210 62 L210 82 L196 82 L196 62 A18 18 0 0 0 160 62 L160 82 L146 82 L146 62 A18 18 0 0 0 110 62 L110 82 L44 82 Z"/>
<path class="s" d="M40 30 L280 30 M44 36 L276 36 L276 82 L246 82 L246 62 A18 18 0 0 0 210 62 L210 82 L196 82 L196 62 A18 18 0 0 0 160 62 L160 82 L146 82 L146 62 A18 18 0 0 0 110 62 L110 82 L44 82 Z"/>
<path class="s" d="M52 30 L52 36 M64 30 L64 36 M76 30 L76 36 M88 30 L88 36 M100 30 L100 36 M112 30 L112 36 M124 30 L124 36 M136 30 L136 36 M148 30 L148 36 M160 30 L160 36 M172 30 L172 36 M184 30 L184 36 M196 30 L196 36 M208 30 L208 36 M220 30 L220 36 M232 30 L232 36 M244 30 L244 36 M256 30 L256 36 M268 30 L268 36"/>
<text class="lb" x="8" y="126">From the side</text>
<path class="w" d="M20 160 C60 156 100 164 160 160 C220 156 260 164 300 160 L300 168 L20 168 Z"/>
<path class="t" d="M160 128 L160 162" stroke-width="3"/>
<path class="s" d="M60 146 L130 146 M126 142 L131 146 L126 150"/>
<text class="lb" x="30" y="140">the view from the house</text>
<text class="lb i" x="172" y="140">the bridge</text>
''', 'Three arches from the terrace. One plank from the side.')

# 3. The Pergola: a garden raised on tunnel spoil
SVG['pergola'] = wrap('pergola', '0 0 320 165', '''
<text class="lb" x="8" y="14">1904</text>
<path class="s" d="M8 106 C40 102 80 110 140 104"/>
<path class="s" d="M60 106 L60 84 L86 84 L86 106 M66 84 L73 76 L80 84"/>
<text class="lb" x="40" y="126">the house, at ground level</text>
<text class="lb" x="176" y="14">1906 onwards</text>
<path class="f" d="M176 104 L176 58 L308 58 L308 100 C290 104 240 108 176 104 Z"/>
<path class="s" d="M176 104 L176 58 L308 58 L308 100"/>
<path class="s" d="M168 106 C200 102 250 110 312 104"/>
<path class="t" d="M186 58 L186 34 M212 58 L212 34 M238 58 L238 34 M264 58 L264 34 M290 58 L290 34 M180 34 L296 34 M180 30 L296 30"/>
<path class="t" d="M200 40 C204 46 200 50 206 54 M226 40 C230 46 226 50 232 54 M252 40 C256 46 252 50 258 54 M278 40 C282 46 278 50 284 54" stroke-dasharray="1.5 2"/>
<text class="lb i" x="196" y="82">tunnel spoil</text>
<circle class="s" cx="196" cy="144" r="11"/>
<path class="s" d="M187 144 L205 144 M196 135 L196 153" opacity=".4"/>
<path class="t" stroke-dasharray="2.5 2.5" d="M204 134 L236 100 M229 101 L237 99 L236 107"/>
<text class="lb" x="212" y="148">the Northern line</text>
<text class="lb i" x="228" y="126">spoil, by cart</text>
''', 'The terrace you walk on is the inside of the Hampstead tunnel, carried up the hill a cartload at a time.')

# 4. The Admiralty shutter telegraph
SVG['telegraph'] = wrap('telegraph', '0 0 320 130', '''
<path class="s" d="M52 122 L52 96 M30 96 L74 96 M30 26 L74 26 M30 26 L30 96 M74 26 L74 96 M52 26 L52 96"/>
<rect class="f" x="34" y="30" width="15" height="18"/><rect class="s" x="34" y="30" width="15" height="18"/>
<path class="s" d="M55 30 L70 30 L70 48 L55 48 Z" fill="none"/>
<path class="s" d="M34 52 L49 52 L49 70 L34 70 Z" fill="none"/>
<rect class="f" x="55" y="52" width="15" height="18"/><rect class="s" x="55" y="52" width="15" height="18"/>
<rect class="f" x="34" y="74" width="15" height="18"/><rect class="s" x="34" y="74" width="15" height="18"/>
<rect class="f" x="55" y="74" width="15" height="18"/><rect class="s" x="55" y="74" width="15" height="18"/>
<text class="lb" x="10" y="14">six shutters</text>
<path class="s" d="M100 70 L314 70" opacity=".4"/>
<path class="t" stroke-dasharray="2 3" d="M100 66 C122 40 148 40 170 66 M170 66 C188 44 204 44 222 66 M222 66 C238 46 252 46 268 66 M268 66 C284 46 298 46 314 66"/>
<circle class="s" cx="100" cy="70" r="4" fill="none"/>
<circle class="f" cx="170" cy="70" r="6"/><circle class="t" cx="170" cy="70" r="6"/>
<circle class="s" cx="222" cy="70" r="4" fill="none"/><circle class="s" cx="268" cy="70" r="4" fill="none"/><circle class="s" cx="314" cy="70" r="4" fill="none"/>
<text class="lb" x="100" y="90" text-anchor="middle">Admiralty</text>
<text class="lb i" x="170" y="90" text-anchor="middle">Hampstead</text>
<text class="lb" x="316" y="90" text-anchor="end">Gt Yarmouth</text>
<text class="lb" x="205" y="110" text-anchor="middle">hilltop to hilltop, by line of sight, in minutes</text>
''', 'Open and shut the six shutters in patterns and the next hill reads the letter. Whitestone Pond was the London end of the coast.')

# 5. The Hampstead pond chain
SVG['pond-chain'] = wrap('pond-chain', '0 0 320 150', '''
<path class="s" d="M6 30 L56 30 L64 62 L114 62 L122 94 L172 94 L180 126 L230 126 L238 140 L310 140" opacity=".35"/>
<path class="w" d="M8 30 C18 24 46 24 56 30 L56 34 L8 34 Z"/>
<path class="w" d="M66 62 C76 56 104 56 114 62 L114 66 L66 66 Z"/>
<path class="w" d="M124 94 C134 88 162 88 172 94 L172 98 L124 98 Z"/>
<path class="w" d="M182 126 C192 120 220 120 230 126 L230 130 L182 130 Z"/>
<path class="f" d="M56 26 L64 26 L64 62 L56 62 Z M114 58 L122 58 L122 94 L114 94 Z M172 90 L180 90 L180 126 L172 126 Z M230 122 L238 122 L238 140 L230 140 Z"/>
<path class="t" d="M56 26 L64 26 M114 58 L122 58 M172 90 L180 90 M230 122 L238 122" stroke-width="2.5"/>
<path class="t" stroke-dasharray="1.5 2" d="M54 22 L66 22 M112 54 L124 54 M170 86 L182 86 M228 118 L240 118"/>
<text class="lb wt" x="8" y="46">Vale of Health</text>
<text class="lb wt" x="66" y="78">Mixed Bathing</text>
<text class="lb wt" x="124" y="110">No. 2</text>
<text class="lb wt" x="182" y="142">No. 1</text>
<text class="lb i" x="72" y="20">the path is the dam</text>
<path class="s" d="M246 140 L310 140 M304 136 L310 140 L304 144"/>
<text class="lb" x="248" y="134">to the Fleet</text>
''', 'Four reservoirs stepped down the valley of the Fleet. What you walk across between them is not a path with a pond either side. It is the dam.')
