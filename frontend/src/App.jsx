
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Toaster } from '@/components/ui/toaster';
import Layout from '@/components/Layout';
import HomePage from '@/pages/HomePage';
import SummarizePage from './components/SummarizePage';
import QAPage from './components/QAPage';
import TextToSpeechPage from './components/TextToSpeechPage';
import PdfOcrPage from './components/PdfOcrPage';
import RoadmapPage from './components/RoadmapPage';


function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/summarize" element={<SummarizePage />} />
          <Route path="/generate-qa" element={<QAPage />} />
          <Route path="/text-to-speech" element={<TextToSpeechPage />} />
          <Route path="/pdf-ocr" element={<PdfOcrPage />} />
          <Route path="/roadmap" element={<RoadmapPage />} />
          
          {/* Add other routes here as pages are created */}
        </Routes>
      </Layout>
      <Toaster />
    </Router>
  );
}

export default App;
  