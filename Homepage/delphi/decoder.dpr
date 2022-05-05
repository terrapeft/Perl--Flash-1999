program decoder;

uses
  Forms,
  _decoder in '_decoder.pas' {Form1};

{$R *.RES}

begin
  Application.Initialize;
  Application.CreateForm(TForm1, Form1);
  Application.Run;
end.
