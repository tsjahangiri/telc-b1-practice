import Foundation
import Vision
import AppKit
// usage: ocr <image> ; prints recognized lines top-to-bottom with x position
let path = CommandLine.arguments[1]
guard let img = NSImage(contentsOfFile: path), let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else { print("ERR load"); exit(1) }
let req = VNRecognizeTextRequest()
req.recognitionLevel = .accurate
req.recognitionLanguages = ["de-DE"]
req.usesLanguageCorrection = false
let h = VNImageRequestHandler(cgImage: cg, options: [:])
try h.perform([req])
var rows: [(Double, Double, String, Float)] = []
for o in req.results ?? [] {
  if let c = o.topCandidates(1).first {
    let b = o.boundingBox
    rows.append((1 - Double(b.maxY), Double(b.minX), c.string, c.confidence))
  }
}
rows.sort { abs($0.0 - $1.0) < 0.008 ? $0.1 < $1.1 : $0.0 < $1.0 }
for r in rows { print(String(format: "%.3f %.3f %.2f\t%@", r.0, r.1, r.3, r.2)) }
