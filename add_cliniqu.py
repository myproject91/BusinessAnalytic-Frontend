with open('index.html', 'r') as f:
    html = f.read()

# 1. Tambah tab sidebar
old_sidebar = '''                  <button @click="activeSection = 'history'; sidebarOpen = false; loadHistory()"'''
new_sidebar = '''                  <button @click="activeSection = 'cliniqu'; sidebarOpen = false" :class="activeSection === 'cliniqu' ? 'active' : ''" class="sidebar-link w-full text-left px-3 py-2.5 rounded-lg text-sm text-gray-400 flex items-center gap-3">
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" class="flex-shrink-0"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 3c1.93 0 3.5 1.57 3.5 3.5S13.93 13 12 13s-3.5-1.57-3.5-3.5S10.07 6 12 6zm7 13H5v-.23c0-.62.28-1.2.76-1.58C7.47 15.82 9.64 15 12 15s4.53.82 6.24 2.19c.48.38.76.97.76 1.58V19z"/></svg>
                      ClinIQ
                  </button>
                  <button @click="activeSection = 'history'; sidebarOpen = false; loadHistory()"'''
html = html.replace(old_sidebar, new_sidebar)

# 2. Tambah tab mobile nav
old_mobile = '''                  <button @click="activeSection = 'history'; loadHistory()"'''
new_mobile = '''                  <button @click="activeSection = 'cliniqu'" class="flex flex-col items-center gap-1 px-2 py-1" :class="activeSection === 'cliniqu' ? 'text-accent' : 'text-gray-500'">
                      <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 3c1.93 0 3.5 1.57 3.5 3.5S13.93 13 12 13s-3.5-1.57-3.5-3.5S10.07 6 12 6zm7 13H5v-.23c0-.62.28-1.2.76-1.58C7.47 15.82 9.64 15 12 15s4.53.82 6.24 2.19c.48.38.76.97.76 1.58V19z"/></svg>
                      <span class="text-xs">ClinIQ</span>
                  </button>
                  <button @click="activeSection = 'history'; loadHistory()"'''
html = html.replace(old_mobile, new_mobile)

# 3. Tambah section ClinIQ
old_empty = '''                  <!-- Empty state -->'''
new_cliniqu = '''                  <!-- ClinIQ Section -->
                  <template x-if="activeSection === 'cliniqu'">
                      <div class="fade-in space-y-4">
                          <div class="flex items-center gap-3 mb-2">
                              <div class="w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0" style="background: linear-gradient(135deg, #0D6E7A, #1A9BAA); box-shadow: 0 0 16px rgba(13,110,122,0.4)">
                                  <svg width="16" height="16" viewBox="0 0 24 24" fill="white"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 3c1.93 0 3.5 1.57 3.5 3.5S13.93 13 12 13s-3.5-1.57-3.5-3.5S10.07 6 12 6zm7 13H5v-.23c0-.62.28-1.2.76-1.58C7.47 15.82 9.64 15 12 15s4.53.82 6.24 2.19c.48.38.76.97.76 1.58V19z"/></svg>
                              </div>
                              <div>
                                  <p class="text-sm font-bold text-white">ClinIQ</p>
                                  <p class="text-xs text-gray-500 font-mono">Modern Care by AI Power Service</p>
                              </div>
                          </div>

                          <div class="upload-zone rounded-2xl p-8 text-center cursor-pointer"
                               @click="$refs.cliniqFile.click()"
                               @dragover.prevent="$el.classList.add('drag-over')"
                               @dragleave="$el.classList.remove('drag-over')"
                               @drop.prevent="handleCliniqDrop($event)">
                              <input type="file" accept=".csv,.pdf" x-ref="cliniqFile" @change="handleCliniqFile($event)" class="hidden">
                              <div class="w-12 h-12 rounded-xl mx-auto mb-3 flex items-center justify-center" style="background: linear-gradient(135deg, #0D6E7A, #5BC8D5); box-shadow: 0 0 20px rgba(13,110,122,0.3)">
                                  <svg width="20" height="20" viewBox="0 0 24 24" fill="white"><path d="M9 16h6v-6h4l-7-7-7 7h4zm-4 2h14v2H5z"/></svg>
                              </div>
                              <template x-if="!cliniqFile">
                                  <div>
                                      <p class="text-sm font-semibold text-gray-300">Drop CSV atau PDF catatan klinis</p>
                                      <p class="text-xs text-gray-600 mt-1">Discharge Notes · ICU Notes · Outpatient Records</p>
                                  </div>
                              </template>
                              <template x-if="cliniqFile">
                                  <div>
                                      <p class="text-sm font-bold text-white" x-text="cliniqFile.name"></p>
                                      <p class="text-xs mt-1 num" style="color:#1A9BAA" x-text="formatFileSize(cliniqFile.size)"></p>
                                  </div>
                              </template>
                          </div>

                          <button @click="analyzeCliniq()" :disabled="!cliniqFile || cliniqLoading"
                                  class="w-full py-3 rounded-xl text-sm font-bold flex items-center justify-center gap-2"
                                  style="background: linear-gradient(135deg, #0D6E7A, #1A9BAA); color: white; opacity: 1"
                                  :style="(!cliniqFile || cliniqLoading) ? 'opacity:0.4;cursor:not-allowed' : ''">
                              <template x-if="cliniqLoading"><div class="spinner"></div></template>
                              <span x-text="cliniqLoading ? 'Menganalisis...' : 'Analyze Clinical Notes'"></span>
                          </button>

                          <template x-if="cliniqError">
                              <div class="rounded-xl p-4 text-sm" style="background: rgba(255,71,87,0.08); border: 1px solid rgba(255,71,87,0.2); color: #ff4757;" x-text="cliniqError"></div>
                          </template>

                          <template x-if="cliniqDone">
                              <div class="fade-in glass rounded-2xl p-5 text-center space-y-3" style="border-color: rgba(13,110,122,0.3)">
                                  <div class="w-14 h-14 rounded-2xl mx-auto flex items-center justify-center" style="background: rgba(13,110,122,0.2)">
                                      <svg width="28" height="28" viewBox="0 0 24 24" fill="#1A9BAA"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z"/></svg>
                                  </div>
                                  <p class="text-sm font-bold text-white">Laporan Selesai!</p>
                                  <p class="text-xs text-gray-400">PDF ClinIQ sudah didownload otomatis</p>
                                  <button @click="cliniqDone=false; cliniqFile=null"
                                          class="px-4 py-2 rounded-lg text-xs font-semibold text-white"
                                          style="background: rgba(13,110,122,0.3); border: 1px solid rgba(26,155,170,0.3)">
                                      Analisis Lagi
                                  </button>
                              </div>
                          </template>

                          <div class="glass rounded-xl p-4 space-y-2" style="border-color: rgba(13,110,122,0.2)">
                              <p class="section-label" style="color:#1A9BAA">Format CSV</p>
                              <p class="text-xs text-gray-500 font-mono">note_id,text</p>
                              <p class="text-xs text-gray-600 font-mono">N001,"Patient 65yo male, hypertension..."</p>
                              <p class="text-xs text-gray-600 font-mono">N002,"ICU day 2, septic shock..."</p>
                          </div>
                      </div>
                  </template>

                  <!-- Empty state -->'''
html = html.replace(old_empty, new_cliniqu)

# 4. Tambah state dan fungsi ClinIQ di Alpine.js
old_state = "                  historyLoading: false,"
new_state = """                  historyLoading: false,
                  cliniqFile    : null,
                  cliniqLoading : false,
                  cliniqError   : null,
                  cliniqDone    : false,"""
html = html.replace(old_state, new_state)

old_section_title = "                      const map = { dashboard: 'Dashboard', upload: 'Upload Data', insight: 'AI Insight', charts: 'Charts', history: 'History' }"
new_section_title = "                      const map = { dashboard: 'Dashboard', upload: 'Upload Data', insight: 'AI Insight', charts: 'Charts', history: 'History', cliniqu: 'ClinIQ' }"
html = html.replace(old_section_title, new_section_title)

old_export = "                  async exportPDF()"
new_cliniqu_fn = """                  handleCliniqFile(e) {
                      const file = e.target.files[0]
                      if (file) { this.cliniqFile = file; this.cliniqDone = false; this.cliniqError = null }
                  },

                  handleCliniqDrop(e) {
                      const file = e.dataTransfer.files[0]
                      if (file && (file.name.endsWith('.csv') || file.name.endsWith('.pdf'))) {
                          this.cliniqFile = file; this.cliniqDone = false; this.cliniqError = null
                      }
                  },

                  async analyzeCliniq() {
                      if (!this.cliniqFile || this.cliniqLoading) return
                      this.cliniqLoading = true
                      this.cliniqError   = null
                      this.cliniqDone    = false
                      const CLINIQ_URL   = 'https://cliniqu-xxx.railway.app'
                      const endpoint     = this.cliniqFile.name.endsWith('.pdf') ? '/analyze/pdf' : '/analyze/csv'
                      const formData     = new FormData()
                      formData.append('file', this.cliniqFile)
                      try {
                          const res = await fetch(`${CLINIQ_URL}${endpoint}`, {
                              method: 'POST', body: formData
                          })
                          if (!res.ok) throw new Error('Analisis gagal. Cek format file.')
                          const blob = await res.blob()
                          const url  = URL.createObjectURL(blob)
                          const a    = document.createElement('a')
                          a.href = url
                          a.download = 'ClinIQ_Report.pdf'
                          a.click()
                          URL.revokeObjectURL(url)
                          this.cliniqDone = true
                      } catch (e) {
                          this.cliniqError = e.message
                      } finally {
                          this.cliniqLoading = false
                      }
                  },

                  async exportPDF()"""
html = html.replace(old_export, new_cliniqu_fn)

with open('index.html', 'w') as f:
    f.write(html)

print("Patch applied!")
