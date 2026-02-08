import React, { useState, useEffect } from 'react';
import { 
  Home, 
  BookOpen, 
  FileText, 
  Search, 
  Calendar, 
  CheckCircle, 
  Cloud, 
  ExternalLink, 
  ChevronRight,
  Sun,
  Moon,
  Github,
  Mail,
  Linkedin
} from 'lucide-react';

// --- Components & UI Elements ---

const Card = ({ title, children, className = "" }) => (
  <div className={`bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-6 shadow-sm hover:shadow-md transition-all duration-300 ${className}`}>
    {title && <h3 className="text-xl font-bold mb-4 text-slate-800 dark:text-slate-100 flex items-center gap-2">
      {title}
    </h3>}
    {children}
  </div>
);

const JournalButton = ({ name, url }) => (
  <a 
    href={url} 
    target="_blank" 
    rel="noopener noreferrer"
    className="flex items-center justify-between p-3 rounded-xl border border-slate-100 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/50 hover:bg-blue-50 dark:hover:bg-blue-900/20 hover:border-blue-200 transition-all group"
  >
    <span className="text-sm font-medium text-slate-700 dark:text-slate-300 group-hover:text-blue-600 dark:group-hover:text-blue-400">{name}</span>
    <ExternalLink size={14} className="text-slate-400 group-hover:text-blue-500" />
  </a>
);

const App = () => {
  const [activeTab, setActiveTab] = useState('Perspective');
  const [isDarkMode, setIsDarkMode] = useState(false);
  const [reminders, setReminders] = useState([
    { id: 1, text: "Review manuscript for Molecular Cell", completed: false },
    { id: 2, text: "Compute stochastic trajectories for NatA", completed: true },
    { id: 3, text: "Group seminar preparation", completed: false }
  ]);
  const [newReminder, setNewReminder] = useState("");
  const [weather, setWeather] = useState({ temp: 22, condition: "Partly Cloudy", city: "Basel" });

  useEffect(() => {
    // Dark mode class toggle
    if (isDarkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [isDarkMode]);

  const toggleReminder = (id) => {
    setReminders(reminders.map(r => r.id === id ? { ...r, completed: !r.completed } : r));
  };

  const addReminder = (e) => {
    if (e.key === 'Enter' && newReminder.trim()) {
      setReminders([{ id: Date.now(), text: newReminder, completed: false }, ...reminders]);
      setNewReminder("");
    }
  };

  const publications = [
    {
      year: "2025",
      title: "HYPK promotes N-terminal protein acetylation through rapid ribosome exchange of NatA",
      authors: "AM Lentzsch, Z Fan, IU Irshad, et al.",
      journal: "Molecular Cell 85 (24), 4562-4574",
      link: "#"
    },
    {
      year: "2025",
      title: "Predicting gene expression changes from chromatin structure modification",
      authors: "S Senapati, IU Irshad, AK Sharma, H Kumar",
      journal: "npj Systems Biology and Applications 11 (1), 34",
      link: "#"
    },
    {
      year: "2024",
      title: "Understanding the regulation of protein synthesis under stress conditions",
      authors: "IU Irshad, AK Sharma",
      journal: "Biophysical Journal 123 (20), 3627-3639",
      link: "#"
    }
  ];

  const journalsByPublisher = {
    "Nature Portfolio": [
      { name: "Nature", url: "https://www.nature.com/" },
      { name: "Nature Physics", url: "https://www.nature.com/nphys/" },
      { name: "Nature Communications", url: "https://www.nature.com/ncomms/" },
      { name: "Nature Methods", url: "https://www.nature.com/nmeth/" },
      { name: "Scientific Reports", url: "https://www.nature.com/srep/" }
    ],
    "Science / AAAS": [
      { name: "Science", url: "https://www.science.org/" },
      { name: "Science Advances", url: "https://www.science.org/journal/sciadv" },
      { name: "Science Signaling", url: "https://www.science.org/journal/stke" }
    ],
    "Cell Press": [
      { name: "Cell", url: "https://www.cell.com/cell/home" },
      { name: "Molecular Cell", url: "https://www.cell.com/molecular-cell/home" },
      { name: "Biophysical Journal", url: "https://www.cell.com/biophysj/home" },
      { name: "Cell Reports", url: "https://www.cell.com/cell-reports/home" }
    ],
    "Physical Societies & Others": [
      { name: "Physical Review Letters", url: "https://journals.aps.org/prl/" },
      { name: "Physical Review E", url: "https://journals.aps.org/pre/" },
      { name: "PNAS", url: "https://www.pnas.org/" },
      { name: "Nucleic Acids Research", url: "https://academic.oup.com/nar" }
    ]
  };

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-950 flex font-sans transition-colors duration-500">
      
      {/* --- Sidebar Navigation --- */}
      <nav className="w-72 border-r border-slate-200 dark:border-slate-800 bg-white/80 dark:bg-slate-900/80 backdrop-blur-xl flex flex-col fixed h-full z-20">
        <div className="p-8">
          <div className="flex items-center gap-3 mb-12">
            <div className="w-10 h-10 bg-blue-600 rounded-xl flex items-center justify-center text-white font-bold text-xl">I</div>
            <span className="font-black text-xl tracking-tight text-slate-900 dark:text-white">INAYAT NODE</span>
          </div>

          <div className="space-y-2">
            {[
              { id: 'Perspective', icon: Home, label: 'Perspective' },
              { id: 'Archive', icon: BookOpen, label: 'Journal Archive' },
              { id: 'Works', icon: FileText, label: 'Selected Works' },
              { id: 'Terminal', icon: Search, label: 'Discovery Terminal' }
            ].map((item) => (
              <button
                key={item.id}
                onClick={() => setActiveTab(item.id)}
                className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition-all ${
                  activeTab === item.id 
                    ? 'bg-blue-600 text-white shadow-lg shadow-blue-500/20' 
                    : 'text-slate-500 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800'
                }`}
              >
                <item.icon size={20} />
                <span className="font-semibold text-sm">{item.label}</span>
              </button>
            ))}
          </div>
        </div>

        <div className="mt-auto p-8 space-y-4">
          <div className="flex justify-between items-center mb-4">
            <button 
              onClick={() => setIsDarkMode(!isDarkMode)}
              className="p-2 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300"
            >
              {isDarkMode ? <Sun size={18} /> : <Moon size={18} />}
            </button>
            <div className="flex gap-2">
               <Mail size={18} className="text-slate-400 cursor-pointer hover:text-blue-500" />
               <Linkedin size={18} className="text-slate-400 cursor-pointer hover:text-blue-500" />
            </div>
          </div>
          <p className="text-[10px] uppercase tracking-widest text-slate-400 font-bold">Postdoctoral Researcher</p>
          <p className="text-xs text-slate-500 dark:text-slate-400">Theoretical Biophysics</p>
        </div>
      </nav>

      {/* --- Main Content Area --- */}
      <main className="flex-1 ml-72 p-12 overflow-y-auto">
        
        {/* --- Top Bar Stats/Widgets --- */}
        <header className="flex justify-between items-start mb-12">
          <div>
            <h2 className="text-sm font-bold text-blue-600 uppercase tracking-widest mb-1">
              {activeTab === 'Perspective' ? 'Dashboard' : activeTab}
            </h2>
            <h1 className="text-4xl font-black text-slate-900 dark:text-white tracking-tighter">
              {activeTab === 'Perspective' ? 'Research Overview' : activeTab === 'Archive' ? 'Global Journal Directory' : 'System Terminal'}
            </h1>
          </div>

          <div className="flex gap-4">
            {/* Weather Widget */}
            <div className="flex items-center gap-3 px-4 py-2 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl shadow-sm">
              <div className="p-2 bg-yellow-100 dark:bg-yellow-900/30 rounded-lg text-yellow-600">
                <Cloud size={18} />
              </div>
              <div>
                <p className="text-[10px] font-bold text-slate-400 uppercase leading-none">{weather.city}</p>
                <p className="text-sm font-bold text-slate-800 dark:text-white leading-none mt-1">{weather.temp}°C · {weather.condition}</p>
              </div>
            </div>

            {/* Date Widget */}
            <div className="flex items-center gap-3 px-4 py-2 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl shadow-sm">
              <div className="p-2 bg-blue-100 dark:bg-blue-900/30 rounded-lg text-blue-600">
                <Calendar size={18} />
              </div>
              <div>
                <p className="text-[10px] font-bold text-slate-400 uppercase leading-none">Calendar</p>
                <p className="text-sm font-bold text-slate-800 dark:text-white leading-none mt-1">Feb 08, 2026</p>
              </div>
            </div>
          </div>
        </header>

        {/* --- Dynamic Content --- */}
        {activeTab === 'Perspective' && (
          <div className="grid grid-cols-12 gap-8">
            <div className="col-span-8 space-y-8">
              <Card className="relative overflow-hidden group">
                <div className="absolute top-0 right-0 w-64 h-64 bg-blue-500/5 rounded-full -mr-20 -mt-20 blur-3xl group-hover:bg-blue-500/10 transition-colors" />
                <h3 className="text-2xl font-black mb-4">The Biophysics Framework</h3>
                <p className="text-slate-600 dark:text-slate-400 text-lg leading-relaxed mb-6">
                  Deciphering the stochastic logic of protein synthesis and gene regulation. 
                  My work bridges fundamental physics with ribosome exchange mechanics 
                  and chromatin conformation.
                </p>
                <div className="bg-slate-50 dark:bg-slate-800/50 p-6 rounded-2xl border border-slate-100 dark:border-slate-800 flex justify-center text-2xl font-serif italic text-slate-800 dark:text-slate-200">
                  {"∂ρ/∂t + ∇·J = σ"}
                </div>
              </Card>

              <div className="grid grid-cols-2 gap-8">
                 <Card title="Current Focus">
                    <ul className="space-y-4">
                      <li className="flex gap-3 items-start">
                        <div className="w-2 h-2 rounded-full bg-blue-600 mt-2" />
                        <p className="text-sm text-slate-600 dark:text-slate-400">Investigating NatA ribosome exchange under stress.</p>
                      </li>
                      <li className="flex gap-3 items-start">
                        <div className="w-2 h-2 rounded-full bg-blue-600 mt-2" />
                        <p className="text-sm text-slate-600 dark:text-slate-400">Refining non-equilibrium transport models.</p>
                      </li>
                    </ul>
                 </Card>
                 <Card title="Recent Activity">
                    <div className="space-y-4">
                       <div className="flex items-center justify-between border-b border-slate-50 dark:border-slate-800 pb-2">
                          <span className="text-xs font-bold text-slate-400">LATEST PUB</span>
                          <span className="text-xs font-medium text-blue-600 bg-blue-50 dark:bg-blue-900/30 px-2 py-0.5 rounded">Molecular Cell</span>
                       </div>
                       <p className="text-xs font-medium text-slate-700 dark:text-slate-300">"HYPK promotes N-terminal protein acetylation..."</p>
                    </div>
                 </Card>
              </div>
            </div>

            <div className="col-span-4 space-y-8">
              {/* Reminders / Tasks */}
              <Card title="Research Planner">
                <div className="space-y-3 mb-6">
                  {reminders.map(r => (
                    <div key={r.id} className="flex items-center gap-3 group">
                      <button 
                        onClick={() => toggleReminder(r.id)}
                        className={`w-5 h-5 rounded flex items-center justify-center border transition-all ${
                          r.completed 
                            ? 'bg-green-500 border-green-500 text-white' 
                            : 'border-slate-300 dark:border-slate-700'
                        }`}
                      >
                        {r.completed && <CheckCircle size={14} />}
                      </button>
                      <span className={`text-sm ${r.completed ? 'line-through text-slate-400' : 'text-slate-700 dark:text-slate-300'}`}>
                        {r.text}
                      </span>
                    </div>
                  ))}
                </div>
                <input 
                  type="text" 
                  placeholder="Add new task... (Enter)"
                  className="w-full bg-slate-100 dark:bg-slate-800 border-none rounded-xl px-4 py-3 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all dark:text-white"
                  value={newReminder}
                  onChange={(e) => setNewReminder(e.target.value)}
                  onKeyDown={addReminder}
                />
              </Card>

              {/* Visualization Placeholder */}
              <Card title="System Dynamics">
                <div className="aspect-square bg-slate-100 dark:bg-slate-800 rounded-2xl flex items-center justify-center overflow-hidden border border-dashed border-slate-300 dark:border-slate-700 relative">
                  <img 
                    src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/TASEP_model.png/640px-TASEP_model.png" 
                    className="opacity-50 grayscale hover:grayscale-0 transition-all cursor-pointer"
                    alt="Dynamics Model"
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-slate-900/40 to-transparent flex items-end p-4">
                    <span className="text-[10px] font-bold text-white uppercase tracking-widest">Ribosome Transport Model</span>
                  </div>
                </div>
              </Card>
            </div>
          </div>
        )}

        {activeTab === 'Archive' && (
          <div className="space-y-12">
            {Object.entries(journalsByPublisher).map(([publisher, journals]) => (
              <section key={publisher}>
                <h3 className="text-lg font-black text-slate-800 dark:text-slate-200 mb-6 flex items-center gap-2">
                  <div className="w-1.5 h-6 bg-blue-600 rounded-full" />
                  {publisher}
                </h3>
                <div className="grid grid-cols-4 gap-4">
                  {journals.map(journal => (
                    <JournalButton key={journal.name} name={journal.name} url={journal.url} />
                  ))}
                </div>
              </section>
            ))}
          </div>
        )}

        {activeTab === 'Works' && (
          <div className="max-w-4xl space-y-6">
            {publications.map((pub, idx) => (
              <div 
                key={idx} 
                className="group relative p-8 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl hover:border-blue-500/50 transition-all duration-300"
              >
                <div className="flex justify-between items-start mb-2">
                  <span className="text-blue-600 font-black tracking-widest text-xs uppercase">{pub.year}</span>
                  <ExternalLink size={16} className="text-slate-300 group-hover:text-blue-500 transition-colors" />
                </div>
                <h4 className="text-xl font-bold text-slate-900 dark:text-white mb-3 leading-snug group-hover:text-blue-600 transition-colors">
                  {pub.title}
                </h4>
                <div className="flex flex-wrap gap-x-6 gap-y-2 text-sm">
                   <div className="flex items-center gap-2 text-slate-500 dark:text-slate-400">
                      <span className="font-semibold">Authors:</span> {pub.authors}
                   </div>
                   <div className="flex items-center gap-2 text-blue-600 dark:text-blue-400 italic">
                      {pub.journal}
                   </div>
                </div>
              </div>
            ))}
          </div>
        )}

        {activeTab === 'Terminal' && (
          <div className="max-w-3xl space-y-8">
            <Card>
              <div className="mb-8">
                <h3 className="text-xl font-bold mb-2">Researcher Query Terminal</h3>
                <p className="text-slate-500 text-sm">Cross-reference between curated physics and biology repositories.</p>
              </div>
              <div className="relative">
                <Search className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400" size={20} />
                <input 
                  type="text"
                  placeholder="Search Google Scholar, arXiv, bioRxiv..."
                  className="w-full pl-12 pr-4 py-4 bg-slate-50 dark:bg-slate-800 border-none rounded-2xl focus:ring-2 focus:ring-blue-500 outline-none text-slate-800 dark:text-white font-medium shadow-inner"
                />
              </div>
              <div className="mt-8 flex gap-4">
                <button className="px-6 py-2 bg-slate-900 dark:bg-white dark:text-slate-950 text-white rounded-xl text-sm font-bold hover:scale-105 transition-transform">Search Scholar</button>
                <button className="px-6 py-2 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl text-sm font-bold hover:bg-slate-50 transition-all">Deep Dive arXiv</button>
              </div>
            </Card>

            <div className="grid grid-cols-2 gap-4">
              {[
                { label: "arXiv: Quant Bio", url: "https://arxiv.org/list/q-bio/new" },
                { label: "bioRxiv: Biophysics", url: "https://www.biorxiv.org/collection/biophysics" },
                { label: "UniProt Database", url: "https://www.uniprot.org/" },
                { label: "RCSB Protein Data Bank", url: "https://www.rcsb.org/" }
              ].map(link => (
                <a 
                  key={link.label}
                  href={link.url}
                  target="_blank"
                  className="p-4 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl flex items-center justify-between hover:bg-blue-50 dark:hover:bg-blue-900/20 group"
                >
                  <span className="text-sm font-bold text-slate-700 dark:text-slate-300 group-hover:text-blue-600">{link.label}</span>
                  <ChevronRight size={16} className="text-slate-300 group-hover:text-blue-600" />
                </a>
              ))}
            </div>
          </div>
        )}

      </main>
    </div>
  );
};

export default App;
