# Certificate Generator

This is a simple web application built with Flask that allows users to generate certificates dynamically. The application uses the `reportlab` library to create PDF certificates with custom names.

## Features

- User-friendly interface with Tailwind CSS for styling.
- Dynamically generates certificates with user-provided names.
- Supports custom fonts for certificate text.
- Downloads the generated certificate as a PDF file.

## Project Structure

```
certificate/
│
├── app.py                     # Main Flask application
├── fonts/
│   └── PinyonScript-Regular.ttf  # Custom font for certificates
├── static/
│   ├── CertificateAIBAITCLUB.png # Background image for certificates
│   └── certificateTemplate.png   # (Optional) Another template image
├── templates/
│   └── index.html             # HTML template for the web interface
```

## Prerequisites

- Python 3.7 or higher
- Flask
- ReportLab

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/certificate-generator.git
   cd certificate-generator
   ```

2. Install the required Python packages:

   ```bash
   pip install flask reportlab
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://localhost:8000`.

## Usage

1. Enter your name in the input field on the web page.
2. Click the "সার্টিফিকেট তৈরি করুন" button.
3. The certificate will be generated and downloaded as a PDF file.

## Customization

- **Background Image**: Replace `static/CertificateAIBAITCLUB.png` with your own background image.
- **Font**: Replace `fonts/PinyonScript-Regular.ttf` with your desired font and update the font registration in `app.py`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with ❤️ by [Mushfikur Rahman](http://fb.me/mushfikur.a.k).
- Powered by Flask and ReportLab.